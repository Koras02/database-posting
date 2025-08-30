
import java.util.Arrays;

public class DataProcessExample {

    public static void main(String[] args) {
        // 🐧 1. 데이터 수집 단계
        int[] scores = {88, 95, 72, 68, 92, 76};

        // 🐧 2. 데이터 전처리: 정렬
        Arrays.sort(scores);

        // 🐧 3. 데이터 분석
        int sum = 0;
        for (int score : scores) {
            sum += score;
        }
        double average = (double) sum / scores.length;
        int min = scores[0];
        int max = scores[scores.length - 1];

        // 🐧 4. 결과 출력
        System.out.println("점수: " + Arrays.toString(scores));
        System.out.println("평균: " + average);
        System.out.println("최소: " + min + "최대: " + max);
    }
}
