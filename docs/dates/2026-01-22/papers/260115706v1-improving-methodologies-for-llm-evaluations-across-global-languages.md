---
layout: default
title: Improving Methodologies for LLM Evaluations Across Global Languages
---

# Improving Methodologies for LLM Evaluations Across Global Languages
**arXiv**：[2601.15706v1](https://arxiv.org/abs/2601.15706) · [PDF](https://arxiv.org/pdf/2601.15706.pdf)  
**作者**：Akriti Vij, Benjamin Chua, Darshini Ramiah, En Qi Ng, Mahran Morsidi, Naga Nikshith Gangarapu, Sharmini Johnson, Vanessa Wilfred, Vikneswaran Kumaran, Wan Sie Lee, Wenzhuo Yang, Yongsen Zheng, Bill Black, Boming Xia, Frank Sun, Hao Zhang, Qinghua Lu, Suyu Ma, Yue Liu, Chi-kiu Lo, Fatemeh Azadi, Isar Nejadgholi, Sowmya Vajjala, Agnes Delaborde, Nicolas Rolin, Tom Seimandi, Akiko Murakami, Haruto Ishi, Satoshi Sekine, Takayuki Semitsu, Tasuku Sasaki, Angela Kinuthia, Jean Wangari, Michael Michie, Stephanie Kasaon, Hankyul Baek, Jaewon Noh, Kihyuk Nam, Sang Seo, Sungpil Shin, Taewhi Lee, Yongsu Kim, Daisy Newbold-Harrop, Jessica Wang, Mahmoud Ghanem, Vy Hong  

**一句话要点**：提出多语言安全评估方法以提升全球语言中LLM的安全可靠性

**关键词**：多语言安全评估, LLM作为评判, 人工标注, 文化语境翻译, 危害类别测试, 国际协作

## 3 点简述
- 核心问题：前沿AI模型在全球部署时，安全行为在不同语言和文化背景下的差异与可靠性未知。
- 方法要点：通过国际协作，在十种语言上测试两个开源模型，使用LLM作为评判和人工标注评估五个危害类别。
- 实验或效果：发现安全行为随语言和危害类型变化，并生成改进多语言安全评估的方法论见解。

## 摘要（原文）

> As frontier AI models are deployed globally, it is essential that their behaviour remains safe and reliable across diverse linguistic and cultural contexts. To examine how current model safeguards hold up in such settings, participants from the International Network for Advanced AI Measurement, Evaluation and Science, including representatives from Singapore, Japan, Australia, Canada, the EU, France, Kenya, South Korea and the UK conducted a joint multilingual evaluation exercise. Led by Singapore AISI, two open-weight models were tested across ten languages spanning high and low resourced groups: Cantonese English, Farsi, French, Japanese, Korean, Kiswahili, Malay, Mandarin Chinese and Telugu. Over 6,000 newly translated prompts were evaluated across five harm categories (privacy, non-violent crime, violent crime, intellectual property and jailbreak robustness), using both LLM-as-a-judge and human annotation.
>   The exercise shows how safety behaviours can vary across languages. These include differences in safeguard robustness across languages and harm types and variation in evaluator reliability (LLM-as-judge vs. human review). Further, it also generated methodological insights for improving multilingual safety evaluations, such as the need for culturally contextualised translations, stress-tested evaluator prompts and clearer human annotation guidelines. This work represents an initial step toward a shared framework for multilingual safety testing of advanced AI systems and calls for continued collaboration with the wider research community and industry.

