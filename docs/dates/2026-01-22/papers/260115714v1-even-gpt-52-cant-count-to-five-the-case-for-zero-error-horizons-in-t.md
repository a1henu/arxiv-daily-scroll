---
layout: default
title: Even GPT-5.2 Can't Count to Five: The Case for Zero-Error Horizons in Trustworthy LLMs
---

# Even GPT-5.2 Can't Count to Five: The Case for Zero-Error Horizons in Trustworthy LLMs
**arXiv**：[2601.15714v1](https://arxiv.org/abs/2601.15714) · [PDF](https://arxiv.org/pdf/2601.15714.pdf)  
**作者**：Ryoma Sato  

**一句话要点**：提出零错误视界以评估可信大语言模型在简单任务上的无错范围

**关键词**：零错误视界, 可信大语言模型, 模型评估, 算法能力涌现, 计算加速

## 3 点简述
- 核心问题：大语言模型在简单任务上仍会出错，影响其在安全关键领域的应用可信度
- 方法要点：定义零错误视界，通过评估模型在序列问题上的无错范围来量化其可靠性
- 实验或效果：评估GPT-5.2和Qwen2.5，发现模型在基础算法任务上存在错误，零错误视界与准确性相关但行为不同

## 摘要（原文）

> We propose Zero-Error Horizon (ZEH) for trustworthy LLMs, which represents the maximum range that a model can solve without any errors. While ZEH itself is simple, we demonstrate that evaluating the ZEH of state-of-the-art LLMs yields abundant insights. For example, by evaluating the ZEH of GPT-5.2, we found that GPT-5.2 cannot even compute the parity of a short string like 11000, and GPT-5.2 cannot determine whether the parentheses in ((((()))))) are balanced. This is surprising given the excellent capabilities of GPT-5.2. The fact that LLMs make mistakes on such simple problems serves as an important lesson when applying LLMs to safety-critical domains. By applying ZEH to Qwen2.5 and conducting detailed analysis, we found that while ZEH correlates with accuracy, the detailed behaviors differ, and ZEH provides clues about the emergence of algorithmic capabilities. Finally, while computing ZEH incurs significant computational cost, we discuss how to mitigate this cost by achieving up to one order of magnitude speedup using tree structures and online softmax.

