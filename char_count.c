#include <stdio.h>
int main(){
    char s[200];
    fgets(s, 200, stdin);
    int upper_count = 0, lower_count=0, digit_count=0, spaces_count=0, special_count = 0;

    for(int i = 0; s[i] != '\0'; i++){
        char ch = s[i];
        if (ch>='A' && ch<='Z'){
            upper_count ++;
        }
        else if (ch>='a' && ch<='z'){
            lower_count += 1;
        }
        else if (ch>='0' && ch<='9'){
            digit_count += 1;
        }
        else if (ch == ' '){
            spaces_count += 1;
        }
        else {
            special_count += 1
        }
    }
    printf("uppercase = %d\n", upper_count );
    printf("lowercase = %d\n", lower_count );
    printf("special character = %d\n", special_count );
    printf("spaces = %d\n", spaces_count );

    return 0;

}