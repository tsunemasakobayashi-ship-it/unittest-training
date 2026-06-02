from greeting.greeting import get_greeting  # 関数の場所に合わせて調整
import datetime
from unittest.mock import patch
import pytest


@pytest.mark.parametrize(
    "year, month, day, hour, minute, second, expected_greeting",
    [
        (2026, 6, 2, 5, 0, 0, "Good morning!"),  # 朝の始まり
        (2026, 6, 2, 11, 59, 59, "Good morning!"),  # 朝の終わり際
        (2026, 6, 2, 12, 0, 0, "Good afternoon!"),  # 昼の始まり
        (2026, 6, 2, 17, 59, 59, "Good afternoon!"),  # 昼の終わり際
        (2026, 6, 2, 18, 0, 0, "Good evening!"),  # 夜の始まり
        (2026, 6, 2, 21, 59, 59, "Good evening!"),  # 夜の終わり際
        (2026, 6, 2, 22, 0, 0, "Good night!"),  # 深夜の始まり
        (2026, 6, 2, 0, 0, 0, "Good night!"),  # 日またぎ
        (2026, 6, 2, 4, 59, 59, "Good night!"),  # 朝の手前
    ],
)
def test_get_greeting_with_patch(
    year, month, day, hour, minute, second, expected_greeting
):
    # 1. 関数に渡したい「偽物の現在時刻（本物のdatetimeオブジェクト）」を作る
    fake_now = datetime.datetime(year, month, day, hour, minute, second)

    # 2. 【超重要】src.greetingファイル内の「datetime.datetime」クラスをピンポイントでモックに差し替える
    with patch("src.greeting.greeting.datetime.datetime") as mock_datetime:

        # 3. 「now() が呼ばれたら、さっき作った fake_now を返しなさい」と設定
        mock_datetime.now.return_value = fake_now

        # 4. 実行して検証
        result = get_greeting()
        assert result == expected_greeting
