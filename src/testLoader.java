import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;


public class testLoader {

	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		try{
			String line;

		    String cmd = "python ws.py 01204111 14 1";
		    //System.out.println(cmd);
		    Process p = Runtime.getRuntime().exec(cmd);
		    BufferedReader br = new BufferedReader(new InputStreamReader(p.getInputStream()));
		    BufferedReader in =
		            new BufferedReader(new InputStreamReader(p.getInputStream()));
		    while ((line = in.readLine()) != null) {
		        System.out.println(line); 
		    }
		    in.close();
		} catch (Exception e) {}

	}

}
