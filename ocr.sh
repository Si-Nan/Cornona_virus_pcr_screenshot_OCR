python -W ignore ocr.py $1
parallel -j 3 'sed -e "/\[INFO/d" -e "/WARNING/d" -e "/^$/d" -e "/input/d" {} |sed  -E  -e "s/pred: (.*), with proba.*/\1/" -e "s/ //" |grep -P "(姓名|采样时间|检测结果)" | head -n3 |xargs -n3 -d"\n"|sed  -e "s/姓名//" -e "s/采样时间//" -e "s/检测结果//"  -e "s/[[:digit:]]\{2\}:[[:digit:]]\{2\}:[[:digit:]]\{2\}//" -e "s/：/\t/g" | xargs -I {} echo -e  "{= s:ocr_pic/::; s:.log::; =}""\t{}"' ::: $1/*log 1> $2
