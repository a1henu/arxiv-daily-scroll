---
layout: default
title: Who can we trust? LLM-as-a-jury for Comparative Assessment
---

# Who can we trust? LLM-as-a-jury for Comparative Assessment
**arXiv**：[2602.16610v1](https://arxiv.org/abs/2602.16610) · [PDF](https://arxiv.org/pdf/2602.16610.pdf)  
**作者**：Mengjie Qian, Guangzhi Sun, Mark J. F. Gales, Kate M. Knill  

**一句话要点**：提出BT-sigma模型以解决LLM作为评委时概率不一致导致的排名效果受限问题

**关键词**：大语言模型评估, 成对比较, Bradley-Terry模型, 评委可靠性, 无监督校准, 自然语言生成评估

## 3 点简述
- 核心问题：LLM作为自动评估器时，其比较概率存在不一致性，影响基于概率的排名有效性
- 方法要点：扩展Bradley-Terry模型为BT-sigma，引入评委判别参数，从成对比较中联合推断项目排名和评委可靠性
- 实验或效果：在NLG评估基准数据集上，BT-sigma优于基于平均的聚合方法，判别参数与LLM判断的循环一致性相关

## 摘要（原文）

> Large language models (LLMs) are increasingly applied as automatic evaluators for natural language generation assessment often using pairwise comparative judgements. Existing approaches typically rely on single judges or aggregate multiple judges assuming equal reliability. In practice, LLM judges vary substantially in performance across tasks and aspects, and their judgment probabilities may be biased and inconsistent. Furthermore, human-labelled supervision for judge calibration may be unavailable. We first empirically demonstrate that inconsistencies in LLM comparison probabilities exist and show that it limits the effectiveness of direct probability-based ranking. To address this, we study the LLM-as-a-jury setting and propose BT-sigma, a judge-aware extension of the Bradley-Terry model that introduces a discriminator parameter for each judge to jointly infer item rankings and judge reliability from pairwise comparisons alone. Experiments on benchmark NLG evaluation datasets show that BT-sigma consistently outperforms averaging-based aggregation methods, and that the learned discriminator strongly correlates with independent measures of the cycle consistency of LLM judgments. Further analysis reveals that BT-sigma can be interpreted as an unsupervised calibration mechanism that improves aggregation by modelling judge reliability.

