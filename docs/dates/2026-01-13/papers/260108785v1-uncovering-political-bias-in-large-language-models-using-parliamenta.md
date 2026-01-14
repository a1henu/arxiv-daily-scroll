---
layout: default
title: Uncovering Political Bias in Large Language Models using Parliamentary Voting Records
---

# Uncovering Political Bias in Large Language Models using Parliamentary Voting Records
**arXiv**：[2601.08785v1](https://arxiv.org/abs/2601.08785) · [PDF](https://arxiv.org/pdf/2601.08785.pdf)  
**作者**：Jieying Chen, Karen de Jong, Andreas Poole, Jan Burakowski, Elena Elderson Nosti, Joep Windt, Chendi Wang  

**一句话要点**：提出基于议会投票记录构建政治偏见基准的方法，评估大语言模型的政治倾向与偏见。

**关键词**：政治偏见评估, 议会投票记录, 大语言模型基准, 意识形态可视化, 跨国家比较

## 3 点简述
- 核心问题：大语言模型在数字平台和决策系统中的政治偏见缺乏系统性研究，可能产生社会影响。
- 方法要点：通过模型生成的投票预测与真实议会投票记录对齐，构建跨国家政治偏见基准。
- 实验或效果：在荷兰、挪威和西班牙案例中，发现先进大语言模型普遍呈现左倾或中间倾向，并对右翼保守政党存在负面偏见。

## 摘要（原文）

> As large language models (LLMs) become deeply embedded in digital platforms and decision-making systems, concerns about their political biases have grown. While substantial work has examined social biases such as gender and race, systematic studies of political bias remain limited, despite their direct societal impact. This paper introduces a general methodology for constructing political bias benchmarks by aligning model-generated voting predictions with verified parliamentary voting records. We instantiate this methodology in three national case studies: PoliBiasNL (2,701 Dutch parliamentary motions and votes from 15 political parties), PoliBiasNO (10,584 motions and votes from 9 Norwegian parties), and PoliBiasES (2,480 motions and votes from 10 Spanish parties). Across these benchmarks, we assess ideological tendencies and political entity bias in LLM behavior. As part of our evaluation framework, we also propose a method to visualize the ideology of LLMs and political parties in a shared two-dimensional CHES (Chapel Hill Expert Survey) space by linking their voting-based positions to the CHES dimensions, enabling direct and interpretable comparisons between models and real-world political actors. Our experiments reveal fine-grained ideological distinctions: state-of-the-art LLMs consistently display left-leaning or centrist tendencies, alongside clear negative biases toward right-conservative parties. These findings highlight the value of transparent, cross-national evaluation grounded in real parliamentary behavior for understanding and auditing political bias in modern LLMs.

