---
layout: default
title: From RAG to Agentic RAG for Faithful Islamic Question Answering
---

# From RAG to Agentic RAG for Faithful Islamic Question Answering
**arXiv**：[2601.07528v1](https://arxiv.org/abs/2601.07528) · [PDF](https://arxiv.org/pdf/2601.07528.pdf)  
**作者**：Gagan Bhatia, Hamdy Mubarak, Mustafa Jarrar, George Mikros, Fadi Zaraket, Mahmoud Alhirthani, Mutaz Al-Khatib, Logan Cochrane, Kareem Darwish, Rashid Yahiaoui, Firoj Alam  

**一句话要点**：提出基于代理式RAG的伊斯兰问答框架，以提升答案忠实性和避免幻觉。

**关键词**：伊斯兰问答, 代理式检索增强生成, 幻觉检测, 阿拉伯语处理, 基准数据集, 多语言模型

## 3 点简述
- 核心问题：LLMs在伊斯兰问答中易产生未基于证据的幻觉，现有评估方法未能充分检测自由形式幻觉和模型在证据不足时的弃权能力。
- 方法要点：构建ISLAMICFAITHQA基准和伊斯兰建模套件，开发代理式RAG框架，通过结构化工具调用进行迭代证据检索和答案修订。
- 实验或效果：实验显示代理式RAG超越标准RAG，在小模型上实现最优性能，并增强阿拉伯语-英语鲁棒性。

## 摘要（原文）

> LLMs are increasingly used for Islamic question answering, where ungrounded responses may carry serious religious consequences. Yet standard MCQ/MRC-style evaluations do not capture key real-world failure modes, notably free-form hallucinations and whether models appropriately abstain when evidence is lacking. To shed a light on this aspect we introduce ISLAMICFAITHQA, a 3,810-item bilingual (Arabic/English) generative benchmark with atomic single-gold answers, which enables direct measurement of hallucination and abstention. We additionally developed an end-to-end grounded Islamic modelling suite consisting of (i) 25K Arabic text-grounded SFT reasoning pairs, (ii) 5K bilingual preference samples for reward-guided alignment, and (iii) a verse-level Qur'an retrieval corpus of $\sim$6k atomic verses (ayat). Building on these resources, we develop an agentic Quran-grounding framework (agentic RAG) that uses structured tool calls for iterative evidence seeking and answer revision. Experiments across Arabic-centric and multilingual LLMs show that retrieval improves correctness and that agentic RAG yields the largest gains beyond standard RAG, achieving state-of-the-art performance and stronger Arabic-English robustness even with a small model (i.e., Qwen3 4B). We will make the experimental resources and datasets publicly available for the community.

