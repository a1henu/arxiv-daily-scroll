---
layout: default
title: Provable Robustness in Multimodal Large Language Models via Feature Space Smoothing
---

# Provable Robustness in Multimodal Large Language Models via Feature Space Smoothing
**arXiv**：[2601.16200v1](https://arxiv.org/abs/2601.16200) · [PDF](https://arxiv.org/pdf/2601.16200.pdf)  
**作者**：Song Xia, Meiwen Ding, Chenqi Kong, Wenhan Yang, Xudong Jiang  

**一句话要点**：提出特征空间平滑以增强多模态大语言模型的对抗鲁棒性

**关键词**：多模态大语言模型, 对抗鲁棒性, 特征空间平滑, 认证保证, 即插即用模块, 白盒攻击

## 3 点简述
- 多模态大语言模型易受对抗扰动攻击，导致特征表示失真和预测错误
- 特征空间平滑方法通过理论证明提供特征余弦相似度的认证下界，确保鲁棒性
- 引入即插即用模块PSM提升高斯鲁棒分数，实验显示攻击成功率从90%降至1%

## 摘要（原文）

> Multimodal large language models (MLLMs) exhibit strong capabilities across diverse applications, yet remain vulnerable to adversarial perturbations that distort their feature representations and induce erroneous predictions. To address this vulnerability, we propose the Feature-space Smoothing (FS) and theoretically prove that FS offers certified robustness on the feature representations of MLLMs. Specifically, FS transforms any feature encoder into a smoothed variant that is guaranteed to maintain a certified lower bound on the feature cosine similarity between clean and adversarial representations under $\ell_2$-bounded attacks. Moreover, we indicate that the value of this Feature Cosine Similarity Bound (FCSB) derived from FS can be improved by enlarging the defined Gaussian robustness score on the vanilla encoder. Building upon this, we introduce the Purifier and Smoothness Mapper (PSM), a plug-and-play module that improves the Gaussian robustness score of MLLMs and thus enhances their certified robustness under FS, without requiring any retraining on MLLMs. We demonstrate that the FS with PSM not only provides a strong theoretical robustness guarantee but also exhibits superior empirical performance compared to adversarial training. Extensive experiments across diverse MLLMs and downstream tasks indicate the effectiveness of the FS-PSM, reducing the Attack Success Rate (ASR) of various white-box attacks from nearly 90\% to about 1\%.

