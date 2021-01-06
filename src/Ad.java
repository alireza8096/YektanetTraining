public class Ad extends BaseAdvertising {


    private String title;
    private String imageUrl;
    private String link;
    private Advertiser advertiser;


    public Ad(int id, String title, String imageUrl, String link, Advertiser advertiser) {
        super(id);
        this.title = title;
        this.imageUrl = imageUrl;
        this.link = link;
        this.advertiser = advertiser;
    }

    public void incViews() {
        super.incViews();
        advertiser.incViews();
    }
    public void incClicks() {
        super.incClicks();
        advertiser.incClicks();
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void setImageUrl(String imageUrl) {
        this.imageUrl = imageUrl;
    }

    public void setLink(String link) {
        this.link = link;
    }

    public String getTitle() {
        return title;
    }

    public String getImageUrl() {
        return imageUrl;
    }


    public String getLink() {
        return link;
    }

    public Advertiser getAdvertiser() {
        return advertiser;
    }

    public void setAdvertiser(Advertiser advertiser) {
        this.advertiser = advertiser;
    }

    public String describeMe() {
        return "I am ad class :)";
    }
}
