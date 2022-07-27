class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int carry = 0;
        int idx = 0;
        for (; idx < Math.min(a.length(), b.length()); idx++) {
            int aDigit = a.charAt(a.length() - 1 - idx) - '0';
            int bDigit = b.charAt(b.length() - 1 - idx) - '0';
            int sum = aDigit + bDigit + carry;
            switch (sum) {
                case 0:
                    sb.append(0);
                    carry = 0;
                    break;
                case 1:
                    sb.append(1);
                    carry = 0;
                    break;
                case 2:
                    sb.append(0);
                    carry = 1;
                    break;
                case 3:
                    sb.append(1);
                    carry = 1;
                    break;
            }
        }
        
        String longer = (a.length() > b.length()) ? a : b;
        for (; idx < longer.length(); idx++) {
            int digit = longer.charAt(longer.length() - 1 - idx) - '0';
            int sum = digit + carry;
            switch (sum) {
                case 0:
                    sb.append(0);
                    carry = 0;
                    break;
                case 1:
                    sb.append(1);
                    carry = 0;
                    break;
                case 2:
                    sb.append(0);
                    carry = 1;
                    break;
                case 3:
                    sb.append(1);
                    carry = 1;
                    break;
            }
        }
        
        if (carry > 0) {
            sb.append(carry);
        }
        
        return sb.reverse().toString();
    }
}
