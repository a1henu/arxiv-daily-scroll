---
layout: default
title: Trapped by simplicity: When Transformers fail to learn from noisy features
---

# Trapped by simplicity: When Transformers fail to learn from noisy features
**arXiv**：[2602.08695v1](https://arxiv.org/abs/2602.08695) · [PDF](https://arxiv.org/pdf/2602.08695.pdf)  
**作者**：Evan Peters, Ando Deng, Matheus H. Zambianco, Devin Blankespoor, Achim Kempf  

**一句话要点**：揭示Transformer在特征噪声下学习布尔函数的局限性，并提出敏感性惩罚提升噪声鲁棒性

**关键词**：噪声鲁棒学习, Transformer, 布尔函数, 特征噪声, 敏感性惩罚, k-junta

## 3 点简述
- 研究Transformer在特征噪声下学习布尔函数的噪声鲁棒性问题
- 发现Transformer因偏向简单函数而难以学习随机k-junta，但可通过敏感性惩罚改进
- 实验表明Transformer在k稀疏奇偶和多数函数上成功，但在随机布尔函数上表现不佳

## 摘要（原文）

> Noise is ubiquitous in data used to train large language models, but it is not well understood whether these models are able to correctly generalize to inputs generated without noise. Here, we study noise-robust learning: are transformers trained on data with noisy features able to find a target function that correctly predicts labels for noiseless features? We show that transformers succeed at noise-robust learning for a selection of $k$-sparse parity and majority functions, compared to LSTMs which fail at this task for even modest feature noise. However, we find that transformers typically fail at noise-robust learning of random $k$-juntas, especially when the boolean sensitivity of the optimal solution is smaller than that of the target function. We argue that this failure is due to a combination of two factors: transformers' bias toward simpler functions, combined with an observation that the optimal function for noise-robust learning typically has lower sensitivity than the target function for random boolean functions. We test this hypothesis by exploiting transformers' simplicity bias to trap them in an incorrect solution, but show that transformers can escape this trap by training with an additional loss term penalizing high-sensitivity solutions. Overall, we find that transformers are particularly ineffective for learning boolean functions in the presence of feature noise.

