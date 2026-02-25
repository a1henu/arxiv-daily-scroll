---
layout: default
title: VAUQ: Vision-Aware Uncertainty Quantification for LVLM Self-Evaluation
---

# VAUQ: Vision-Aware Uncertainty Quantification for LVLM Self-Evaluation
**arXiv**：[2602.21054v1](https://arxiv.org/abs/2602.21054) · [PDF](https://arxiv.org/pdf/2602.21054.pdf)  
**作者**：Seongheon Park, Changdae Oh, Hyeong Kyu Choi, Xuefeng Du, Sharon Li  

**一句话要点**：提出VAUQ框架以解决LVLM幻觉问题，通过视觉感知不确定性量化实现自评估。

**关键词**：视觉语言模型, 不确定性量化, 自评估, 幻觉检测, 图像信息分数, 核心区域掩码

## 3 点简述
- 核心问题：LVLM常产生幻觉，现有自评估方法依赖语言先验，不适用于视觉条件预测。
- 方法要点：引入图像信息分数和核心区域掩码策略，结合预测熵进行无训练评分。
- 实验或效果：在多个数据集上，VAUQ一致优于现有自评估方法，提升部署可靠性。

## 摘要（原文）

> Large Vision-Language Models (LVLMs) frequently hallucinate, limiting their safe deployment in real-world applications. Existing LLM self-evaluation methods rely on a model's ability to estimate the correctness of its own outputs, which can improve deployment reliability; however, they depend heavily on language priors and are therefore ill-suited for evaluating vision-conditioned predictions. We propose VAUQ, a vision-aware uncertainty quantification framework for LVLM self-evaluation that explicitly measures how strongly a model's output depends on visual evidence. VAUQ introduces the Image-Information Score (IS), which captures the reduction in predictive uncertainty attributable to visual input, and an unsupervised core-region masking strategy that amplifies the influence of salient regions. Combining predictive entropy with this core-masked IS yields a training-free scoring function that reliably reflects answer correctness. Comprehensive experiments show that VAUQ consistently outperforms existing self-evaluation methods across multiple datasets.

