---
layout: default
title: Robustness and Reasoning Fidelity of Large Language Models in Long-Context Code Question Answering
---

# Robustness and Reasoning Fidelity of Large Language Models in Long-Context Code Question Answering
**arXiv**：[2602.17183v1](https://arxiv.org/abs/2602.17183) · [PDF](https://arxiv.org/pdf/2602.17183.pdf)  
**作者**：Kishan Maharaj, Nandakishore Menon, Ashita Saxena, Srikanth Tamilselvam  

**一句话要点**：评估大语言模型在长代码上下文问答中的鲁棒性与推理保真度

**关键词**：大语言模型, 长代码上下文, 代码问答, 鲁棒性评估, 推理保真度, 控制消融实验

## 3 点简述
- 研究大语言模型在长代码上下文问答中的鲁棒性，关注输入条件变化下的性能表现
- 通过控制消融实验测试对答案格式、干扰项和上下文规模的敏感性，扩展数据集至COBOL和Java
- 结果显示模型在选项打乱、开放式问题和无关信息干扰下性能显著下降，揭示当前评估的局限性

## 摘要（原文）

> Large language models (LLMs) increasingly assist software engineering tasks that require reasoning over long code contexts, yet their robustness under varying input conditions remains unclear. We conduct a systematic study of long-context code question answering using controlled ablations that test sensitivity to answer format, distractors, and context scale. Extending LongCodeBench Python dataset with new COBOL and Java question-answer sets, we evaluate state-of-the-art models under three settings: (i) shuffled multiple-choice options, (ii) open-ended questions and (iii) needle-in-a-haystack contexts containing relevant and adversarially irrelevant information. Results show substantial performance drops in both shuffled multiple-choice options and open-ended questions, and brittle behavior in the presence of irrelevant cues. Our findings highlight limitations of current long-context evaluations and provide a broader benchmark for assessing code reasoning in both legacy and modern systems.

