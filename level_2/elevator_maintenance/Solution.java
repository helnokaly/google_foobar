import java.util.Arrays;
import java.util.stream.Collectors;

public class Solution {
  public static String[] solution(String[] l) {
    return Arrays
      .asList(l)
      .stream()
      .map(i -> new Version(i))
      .sorted()
      .map(i -> i.text)
      .collect(Collectors.toList())
      .toArray(new String[]{});
  }

  // public static void main(String[] args) {
  //   System.out.println(Arrays.toString(Solution.solution(new String[]{"1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"})));
  //   // Output:
  //   //     0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0

  //   System.out.println(Arrays.toString(Solution.solution(new String[]{"1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"})));
  //   // Output:
  //   //     1.0,1.0.2,1.0.12,1.1.2,1.3.3
  // }
}

class Version implements Comparable<Version> {
  public int major = 0;
  public int minor = 0;
  public int revision = 0;
  public String text;
  public int partsCount;

  public Version(String version) {
    this.text = version;
    String[] parts = this.text.split("\\.");
    this.partsCount = parts.length;

    if (this.partsCount == 3) {
      this.major = Integer.parseInt(parts[0]);
      this.minor = Integer.parseInt(parts[1]);
      this.revision = Integer.parseInt(parts[2]);
    } else if (this.partsCount == 2) {
      this.major = Integer.parseInt(parts[0]);
      this.minor = Integer.parseInt(parts[1]);
    } else {
      this.major = Integer.parseInt(parts[0]);
    }
  }

  public int compareTo(Version other) {
    if (this.major < other.major) {
      return -1;
    } else if (this.major > other.major) {
      return 1;
    } else if (this.minor < other.minor) {
      return -1;
    } else if (this.minor > other.minor) {
      return 1;
    } else if (this.revision < other.revision) {
      return -1;
    } else if (this.revision > other.revision) {
      return 1;
    } else {
      return this.partsCount - other.partsCount;
    }
  }
}
