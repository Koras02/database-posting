
public class Study {

    public static void main(String[] args) {
        String[] studys = {"국어", "영어", "수학"};
        int[] scores = {85, 88, 98};

        // 과목별 총점 
        int totalScore = 0;

        System.out.println("--- 과목별 점수 -------");
        for (int i = 0; i < studys.length; i++) {
            System.out.println(studys[i] + " 점수: " + scores[i]);
            totalScore += scores[i]; // 각 과목 점수 totalScore 누적
        }

        // 총점과 평균 계산 
        double average = (double) totalScore / scores.length;

        // 총첨 밎 평균 출력
        System.out.println("총점: " + totalScore);
        System.out.printf("평균: %.2f%n", average);

    }
}
