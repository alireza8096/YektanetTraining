import java.util.ArrayList;

public class Advertiser extends BaseAdvertising {

    private String name;
    private static ArrayList<Advertiser> allAdvertisers = new ArrayList<>();

    public Advertiser(int id, String name) {
        super(id);
        this.name = name;
        allAdvertisers.add(this);
    }

    public static int getTotalClicks() {
        int sum = 0;
        for (Advertiser advertiser : allAdvertisers) {
            sum += advertiser.getClicks();
        }
        return sum;
    }

    public static String help() {
        return "I have id, name, clicks and views fields";
    }
    public String describeMe() {
        return "I am advertiser class :)";
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }


}
