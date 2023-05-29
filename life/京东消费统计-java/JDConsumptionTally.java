import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.File;
import java.io.IOException;

/**
 * @Deacription TODO
 * @Author Zhangmj
 * @Date 2023/5/29 11:15
 * @Version 1.0
 * @DESC 使用方法：打开订单页面根据自己的需求筛选，记得选择已完成的订单。然后ctrl+s保存为html页面。分页的保存多个页面放到一个文件夹下即可统计。
 **/
public class JDConsumptionTally {

    public static void main(String[] args) throws IOException {
        double sum = 0;

        // 指定目录下的3个html文件
        File[] files = new File("C:\\Users\\LD-WX02\\Desktop\\jd\\2022").listFiles();

        for (File file : files) {
            if (file.isFile() && file.getName().endsWith(".html")) {
                // 读取文件内容，转换成Document对象
                Document doc = Jsoup.parse(file, "UTF-8", "");
                // 获取<div class="amount">
                Elements amountDiv = doc.select("div.amount");
                // 获取<span>¥25.62</span>里的文本内容
                for (Element e : amountDiv) {
                    String priceStr = e.selectFirst("span").text();
                    // 将文本内容转换成double类型的数值
                    String[] s = priceStr.split("¥");
                    double price = Double.parseDouble(s[1]);
                    // 累加价格
                    sum += price;
                }
            }
        }

        // 输出结果
        System.out.println("总价格为：" + sum);

    }

}
