---
layout: default
title: Don't Throw Away Your Beams: Improving Consistency-based Uncertainties in LLMs via Beam Search
---

# Don't Throw Away Your Beams: Improving Consistency-based Uncertainties in LLMs via Beam Search
**arXiv**：[2512.09538v1](https://arxiv.org/abs/2512.09538) · [PDF](https://arxiv.org/pdf/2512.09538.pdf)  
**作者**：Ekaterina Fadeeva, Maiya Goloburda, Aleksandr Rubashevskii, Roman Vashurin, Artem Shelmanov, Preslav Nakov, Mrinmaya Sachan, Maxim Panov  

**一句话要点**：提出基于束搜索的一致性方法以改进大语言模型在短问答中的不确定性量化

**关键词**：不确定性量化, 束搜索, 大语言模型, 短问答, 一致性方法

## 3 点简述
- 核心问题：多轮采样在短问答中易产生重复样本，导致不确定性估计方差大。
- 方法要点：使用束搜索生成候选集，替代多轮采样，提升一致性和减少方差。
- 实验或效果：在六个问答数据集上验证，性能优于多轮采样，达到先进水平。

## 摘要（原文）

> Consistency-based methods have emerged as an effective approach to uncertainty quantification (UQ) in large language models. These methods typically rely on several generations obtained via multinomial sampling, measuring their agreement level. However, in short-form QA, multinomial sampling is prone to producing duplicates due to peaked distributions, and its stochasticity introduces considerable variance in uncertainty estimates across runs. We introduce a new family of methods that employ beam search to generate candidates for consistency-based UQ, yielding improved performance and reduced variance compared to multinomial sampling. We also provide a theoretical lower bound on the beam set probability mass under which beam search achieves a smaller error than multinomial sampling. We empirically evaluate our approach on six QA datasets and find that its consistent improvements over multinomial sampling lead to state-of-the-art UQ performance.

