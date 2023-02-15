class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        
        int rows=mat.length;
        int cols=mat[0].length;
        
        //check to see if given parameters are possible and legal for matrix transposing
        if((rows*cols)!=(r*c)){
            return mat;
        }
        
        int[][] matT=new int[r][c];
        int rowsT=0;
        int colsT=0;
        
        //traverse the mat matrix and store values in the new matrix col by col
        for(int i=0; i<rows; i++){
            for(int j=0; j<cols; j++){
                matT[rowsT][colsT] = mat[i][j];
                colsT++;
                
                //if reached end of new cols, reset cols and incrememnt row
                if(colsT == c){
                    colsT = 0;
                    rowsT++;
                }
            }
        }
        return matT;
    }
}