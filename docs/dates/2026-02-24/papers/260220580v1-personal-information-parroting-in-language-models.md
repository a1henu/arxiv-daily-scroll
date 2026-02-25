---
layout: default
title: Personal Information Parroting in Language Models
---

# Personal Information Parroting in Language Models
**arXiv**：[2602.20580v1](https://arxiv.org/abs/2602.20580) · [PDF](https://arxiv.org/pdf/2602.20580.pdf)  
**作者**：Nishant Subramani, Kshitish Ghate, Mona Diab  

**一句话要点**：提出R&R检测器套件以评估语言模型对个人信息的记忆风险

**关键词**：个人信息检测, 语言模型记忆, 隐私风险, 正则表达式检测, 模型规模影响, 预训练数据过滤

## 3 点简述
- 核心问题：语言模型在训练中记忆网络数据中的个人信息，增加隐私泄露风险。
- 方法要点：开发正则表达式和规则检测器，优于现有方法，用于检测电子邮件、电话号码和IP地址。
- 实验或效果：在Pythia模型套件上测试，发现模型大小和预训练量与记忆率正相关，最小模型记忆2.7%实例。

## 摘要（原文）

> Modern language models (LM) are trained on large scrapes of the Web, containing millions of personal information (PI) instances, many of which LMs memorize, increasing privacy risks. In this work, we develop the regexes and rules (R&R) detector suite to detect email addresses, phone numbers, and IP addresses, which outperforms the best regex-based PI detectors. On a manually curated set of 483 instances of PI, we measure memorization: finding that 13.6% are parroted verbatim by the Pythia-6.9b model, i.e., when the model is prompted with the tokens that precede the PI in the original document, greedy decoding generates the entire PI span exactly. We expand this analysis to study models of varying sizes (160M-6.9B) and pretraining time steps (70k-143k iterations) in the Pythia model suite and find that both model size and amount of pretraining are positively correlated with memorization. Even the smallest model, Pythia-160m, parrots 2.7% of the instances exactly. Consequently, we strongly recommend that pretraining datasets be aggressively filtered and anonymized to minimize PI parroting.

