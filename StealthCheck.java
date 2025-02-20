import java.util.Random;
import java.util.Scanner;

public class StealthCheck {
    public static void main(String[] args) {
        Random random = new Random();
        int dice = random.nextInt(20) + 1; // Rolls a dice between 1 and 20
        Scanner scanner = new Scanner(System.in);

        System.out.print("What is your character's level? ");
        String userLevelInput = scanner.nextLine();
        int userLevel = 0;
        
        try {
            userLevel = Integer.parseInt(userLevelInput);
        } catch (NumberFormatException e) {
            System.out.println("Invalid input. Please enter a number for the level.");
            System.exit(1);
        }

        int[] proficiencyBonus = { 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6 };
        
        System.out.print("Do you know your character's dexterity modifier? (Y/N) ");
        String userInput = scanner.nextLine().toLowerCase();

        System.out.print("Do you have proficiency in the Stealth skill? (Y/N) ");
        String stealthProficiency = scanner.nextLine().toLowerCase();
        String stealthExpertise = "n";
        
        if ("y".equals(stealthProficiency)) {
            System.out.print("Do you have expertise in the Stealth skill? (Y/N) ");
            stealthExpertise = scanner.nextLine().toLowerCase();
        }

        int userDexterity = 0;
        if ("y".equals(userInput)) {
            System.out.print("What is your character's dexterity modifier? ");
            try {
                userDexterity = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number for the dexterity modifier.");
                System.exit(1);
            }
        } else if ("n".equals(userInput)) {
            System.out.print("What is your character's dexterity score? ");
            try {
                int dexScore = Integer.parseInt(scanner.nextLine());
                userDexterity = (dexScore - 10) / 2;
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number for the dexterity score.");
                System.exit(1);
            }
        } else {
            System.out.println("Invalid input for dexterity modifier.");
            System.exit(1);
        }

        System.out.println("You rolled a " + dice);

        int stealthCheck = dice + userDexterity;
        if ("y".equals(stealthExpertise)) {
            stealthCheck += proficiencyBonus[userLevel - 1] * 2;
        } else if ("y".equals(stealthProficiency)) {
            stealthCheck += proficiencyBonus[userLevel - 1];
        }

        System.out.println("Your stealth check is " + stealthCheck + ".");
        scanner.close();
    }
}