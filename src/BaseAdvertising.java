public class BaseAdvertising {
    private int id;
    private int clicks;
    private int views;

    public BaseAdvertising(int id) {
        this.id = id;
    }

    public BaseAdvertising() {
    }

    public void incViews() {
        this.views++;
    }
    public void incClicks() {
        this.clicks++;
    }

    public int getClicks() {
        return clicks;
    }

    public int getViews() {
        return views;
    }
    public String describeMe() {
        return "I am BaseAdvertising class :)";
    }
}
