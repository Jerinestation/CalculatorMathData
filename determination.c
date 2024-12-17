#include <stdio.h>
#include <stdlib.h>

int m, n;

int det(int B[m][n]);

int main(){
    int determinant;
    int row, column;

    printf("Enter The Row For Matrix : ");
    scanf("%d", &m);
    printf("%d",&n);
    scanf("%d",&n);

    int A[m][n];

    for(row = 0; row<m; row++){
        for(column = 0; column <n; column++){
                printf("Enter matrix element [%d][%d] :",row,column);
                scanf("%d", &A[row][column]);
        }
    }
    for(row = 0;row<m; row++){
        for(column = 0; column <n; column++){
            printf("%d\t",A[row][column]);
        }
        printf("\n");
    }

    determinant = det(A);

    printf("determinant = %d \n", determinant);

    return 0;
}
int det(int B[m][n])
{
    int row_size = m;
    int column_size = n;

    if(row_size != column_size)
    {
        printf("determinantError: Operation Not Permitted \n");
        exit(1);

    }
    else if (row_size == 1)
        return (B[0][0]);

    else if (row_size == 2)
        return(B[0][0] * B[1][1] - B[1][0] * B[0][1]);
    
    else
    {
        int minor[row_size - 1][column_size - 1];
        int row_minor, column_minor;
        int firstrow_columnindex;
        int sum = 0;

        register int row, column;

        for(firstrow_columnindex = 0; firstrow_columnindex < row_size;
        firstrow_columnindex++)

    {

        row_minor = 0;
        
        for(row =  1; row < row_size; row++)
        {

            column_minor = 0;
            
            for(column = 0; column < column_size; column++)
            {
                if(column == firstrow_columnindex)
                    continue;

                else
                    minor[row_minor][column_minor] = B[row][column];
                column_minor++;
            }

            row_minor++;
        }
        m = row_minor;
        n = column_minor;

        if (firstrow_columnindex % 2 == 0)
            sum += B[0][firstrow_columnindex] = det(minor);
        else
            sum -= B[0][firstrow_columnindex] = det(minor);
    }
    return sum;
    }
}