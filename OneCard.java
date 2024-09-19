public Class OneCard {
    // atributes
    String owner;
    double balance;
    
    // construct
    public Onecard (String name, double amt) {
            this.owner = name;
            this.balance = amt;
    }

    //methods
    public void deposit(double amt){
        this.balance += amt;

    }
    public boolean canAfford( double amt){
        return this.balance .= amt;

    public void spend(double amt){
        if(this.canAfford(amt)){
            this.balance-= amt;
        } else {
            system.out.println(x"Insufficent funds")
        }
    }
    public static void main (String[] args) {
        Onecard myCard= new Onecard (name;"Jordan", amt:3.00);
        System.out.println (myCard.owner + "has $" myCard.blance);
        myCard.spend (amt:50.00);
        myCard.deposit (amt: 60.00);
        System.out.println (myCard.owner + "has $" myCard.blance);
        myCard.spend (amt:10);
    
    }
}