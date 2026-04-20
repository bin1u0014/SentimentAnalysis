"""전체 환경 세팅 검증 스크립트"""
import sys

def test_python_packages():
    packages = [
        "torch", "transformers", "xgboost",
        "pandas", "yfinance", "clearml",
        "fastapi", "boto3", "shap"
    ]
    failed = []
    for pkg in packages:
        try:
            __import__(pkg)
            print(f"  ✓ {pkg}")
        except ImportError:
            print(f"  ✗ {pkg} — 설치 필요")
            failed.append(pkg)
    return len(failed) == 0

def test_mps():
    import torch
    available = torch.backends.mps.is_available()
    print(f"  {'✓' if available else '✗'} Apple MPS — {'사용 가능' if available else '비활성'}")
    return available

def test_clearml():
    try:
        from clearml import Task
        task = Task.init(
            project_name="SentimentAnalysis",
            task_name="setup-test",
            task_type=Task.TaskTypes.testing
        )
        task.close()
        print("  ✓ ClearML 연결 성공")
        return True
    except Exception as e:
        print(f"  ✗ ClearML 연결 실패: {e}")
        return False

def test_aws():
    try:
        import boto3
        from dotenv import load_dotenv
        load_dotenv()
        s3 = boto3.client("s3", region_name="ap-southeast-2")
        s3.list_buckets()
        print("  ✓ AWS S3 연결 성공")
        return True
    except Exception as e:
        print(f"  ✗ AWS 연결 실패: {e}")
        return False

if __name__ == "__main__":
    print("\n=== SentimentAnalysis 환경 세팅 검증 ===\n")
    print("[1] Python 패키지:")
    r1 = test_python_packages()
    print("\n[2] Apple Silicon MPS:")
    r2 = test_mps()
    print("\n[3] ClearML:")
    r3 = test_clearml()
    print("\n[4] AWS:")
    r4 = test_aws()

    print("\n" + "="*40)
    if r1 and r3:
        print("✅ 핵심 세팅 완료! Stage 2로 진행하세요.")
    else:
        print("⚠️  일부 항목 확인 필요. 위 오류를 수정 후 재실행하세요.")
    sys.exit(0 if (r1 and r3) else 1)