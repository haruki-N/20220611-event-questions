def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    """

    :param sorted_array: list of int sorted in accending order
    :param target_number: target number that you want to find
    :return: the idx of target_number if target_number exists in sorted_array else -1
    """
    candidate_array = sorted_array   # 探索対象のarray
    while len(candidate_array) > 0:   # 探索対象とするarrayに要素が存在する限り繰り返す
        center_index = len(candidate_array)//2
        center_value = candidate_array[center_index]   # 比較対象とする要素

        if center_value == target_number:   # center_valueと合致した場合は探索終了
            return center_value

        elif center_value > target_number:
            candidate_array = candidate_array[:center_index]   # center_valueより小さい値を探索対象とする

        else:
            candidate_array = candidate_array[center_index+1:]   # center_valueより大きい値を探索対象とする

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
