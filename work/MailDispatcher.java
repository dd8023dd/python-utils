import cn.hutool.core.io.file.FileReader;
import lombok.SneakyThrows;
import lombok.extern.slf4j.Slf4j;

import java.io.IOException;
import java.util.*;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;
import javax.mail.*;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;
import javax.mail.search.OrTerm;
import javax.mail.search.SearchTerm;
import javax.mail.search.SubjectTerm;

public class MailDispatcher {

    private static final String IMAP_HOST = "imap.qiye.aliyun.com";
    private static final String IMAP_USERNAME = "user";
    private static final String IMAP_PASSWORD = "password";
    private static final String SMTP_HOST = "smtp.qiye.aliyun.com";

    // 设置线程池大小为5，线程池最大大小为10，线程池空闲时间为10秒
    static ThreadPoolExecutor executor = new ThreadPoolExecutor(5, 10, 10, TimeUnit.SECONDS, new LinkedBlockingQueue<>());

    public static void main(String[] args) throws MessagingException, IOException, InterruptedException {
        Properties props = new Properties();
        props.setProperty("mail.transport.protocol", "imap");
        props.setProperty("mail.imap.host", IMAP_HOST);
        props.setProperty("mail.imap.connectiontimeout", "1000000");
        props.setProperty("mail.imap.timeout", "1000000");
        props.setProperty("mail.imap.socketFactory.class", "javax.net.ssl.SSLSocketFactory");
        props.setProperty("mail.imap.socketFactory.fallback", "false");
        props.setProperty("mail.imap.port", "993");
        props.setProperty("mail.imap.socketFactory.port", "993");

        Session session  = Session.getInstance(props);
        Store store = session.getStore("imap");

        store.connect(IMAP_HOST, 993, IMAP_USERNAME, IMAP_PASSWORD);

        Folder inbox = store.getFolder("INBOX");
        inbox.open(Folder.READ_WRITE);
        Message[] search = inbox.getMessages();
        List<Message> messages = Arrays.asList(search);
        List<List<Message>> slice = slice(messages, 100);
        //对list分片

        Properties properties = new Properties();
        // 发送短信服务器地址 可以是域名或者ip地址
        properties.setProperty("mail.host",SMTP_HOST);
        // 短信发送协议默认为smtp协议
        properties.setProperty("mail.transport.protocol", "smtp");
        properties.setProperty("mail.smtp.auth", "true");
        properties.setProperty("mail.smtp.socketFactory.class", "javax.net.ssl.SSLSocketFactory");
        properties.setProperty("mail.smtp.socketFactory.port", "465");
        properties.setProperty("mail.smtp.port", "465");
        properties.setProperty("mail.smtp.ssl.enable","true");
        properties.setProperty("mail.mime.splitlongparameters","false");
        final Session session2 = Session.getInstance(properties);
        Transport ts = session2.getTransport();
        ts.connect(SMTP_HOST,IMAP_USERNAME, IMAP_PASSWORD);
        /*使用JavaMail发送邮件的5个步骤*/
        String rpath = "C:\\Users\\LD-WX02\\Desktop\\需要过滤的主题.txt";
        FileReader fileReader = new FileReader(rpath);
        List<String> lines = fileReader.readLines();
        Set<String> filters = new HashSet<>(lines);
        for (List<Message> ms : slice) {
            executor.execute(new Runnable() {
                @SneakyThrows
                @Override
                public void run() {
                    for (Message message : ms) {
                        add();
                        // 判断邮件是否包含指定关键词
                        try {
                            String subject = message.getSubject();
                            if(filters.contains(subject)){
                                continue;
                            }
                            if (subject != null && (subject.contains("净值") || subject.contains("估值"))) {
                                // 处理匹配的邮件
                                String to = "to@to.com";
                                MimeMessage forward = new MimeMessage(session2);
                                forward.setSubject(subject);
                                if( message.getContent() instanceof String){
                                    forward.setText(message.getContent().toString());
                                }else {
                                    forward.setContent((Multipart) message.getContent());
                                }
                                forward.setFrom(new InternetAddress(IMAP_USERNAME));
                                forward.addRecipient(Message.RecipientType.TO, new InternetAddress(to));
                                ts.sendMessage(forward,forward.getAllRecipients());
                                System.out.println("主题[" + subject + "]Email sent successfully to:"+ to);
                            }
                        }catch (Exception e) {
                            System.out.println(e);
                        }

                    }
                }
            });

        }
        while (i<=messages.size()) {
            Thread.sleep(1000);
        }
        inbox.close(true);
        store.close();

        System.out.println("Finished.");
    }

    public static int i = 0;

    public static void add(){
        i++;
    }


    public static <T> List<List<T>> slice(List<T> list, int chunkSize) {
        List<List<T>> slices = new ArrayList<>();
        int size = list.size();
        for (int i = 0; i < size; i += chunkSize) {
            int end = Math.min(size, i + chunkSize);
            slices.add(list.subList(i, end));
        }
        return slices;
    }

}
