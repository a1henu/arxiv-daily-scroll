---
layout: default
title: Two Pathways to Truthfulness: On the Intrinsic Encoding of LLM Hallucinations
---

# Two Pathways to Truthfulness: On the Intrinsic Encoding of LLM Hallucinations
**arXiv**：[2601.07422v1](https://arxiv.org/abs/2601.07422) · [PDF](https://arxiv.org/pdf/2601.07422.pdf)  
**作者**：Wen Luo, Guangyue Peng, Wei Li, Shaohang Wei, Feifan Song, Liang Wang, Nan Yang, Xingxing Zhang, Jing Jin, Furu Wei, Houfeng Wang  

**一句话要点**：揭示大语言模型幻觉编码的双通路机制，以提升检测性能

**关键词**：大语言模型幻觉, 真实性编码, 注意力机制, 知识边界, 幻觉检测

## 3 点简述
- 核心问题：大语言模型内部状态如何编码真实性信号，机制不明。
- 方法要点：通过注意力敲除和令牌修补，分离问题锚定和答案锚定通路。
- 实验或效果：发现通路与知识边界相关，并应用于增强幻觉检测。

## 摘要（原文）

> Despite their impressive capabilities, large language models (LLMs) frequently generate hallucinations. Previous work shows that their internal states encode rich signals of truthfulness, yet the origins and mechanisms of these signals remain unclear. In this paper, we demonstrate that truthfulness cues arise from two distinct information pathways: (1) a Question-Anchored pathway that depends on question-answer information flow, and (2) an Answer-Anchored pathway that derives self-contained evidence from the generated answer itself. First, we validate and disentangle these pathways through attention knockout and token patching. Afterwards, we uncover notable and intriguing properties of these two mechanisms. Further experiments reveal that (1) the two mechanisms are closely associated with LLM knowledge boundaries; and (2) internal representations are aware of their distinctions. Finally, building on these insightful findings, two applications are proposed to enhance hallucination detection performance. Overall, our work provides new insight into how LLMs internally encode truthfulness, offering directions for more reliable and self-aware generative systems.

