---
layout: default
title: Observationally Informed Adaptive Causal Experimental Design
---

# Observationally Informed Adaptive Causal Experimental Design
**arXiv**：[2603.03785v1](https://arxiv.org/abs/2603.03785) · [PDF](https://arxiv.org/pdf/2603.03785.pdf)  
**作者**：Erdun Gao, Liang Zhang, Jake Fawkes, Aoqi Zuo, Wenqin Liu, Haoxuan Li, Mingming Gong, Dino Sejdinovic  

**一句话要点**：提出R-Design框架，利用观测数据作为先验，高效修正因果估计中的观测偏差。

**关键词**：因果推断, 实验设计, 观测数据, 残差学习, 信息增益

## 3 点简述
- 核心问题：随机对照试验稀缺，观测数据因偏差担忧未被用于前瞻性试验设计。
- 方法要点：引入Active Residual Learning，通过估计残差修正观测偏差，提出R-EPIG准则优化实验设计。
- 实验或效果：在合成和半合成基准测试中，R-Design显著优于基线方法，验证了效率优势。

## 摘要（原文）

> Randomized Controlled Trials (RCTs) represent the gold standard for causal inference yet remain a scarce resource. While large-scale observational data is often available, it is utilized only for retrospective fusion, and remains discarded in prospective trial design due to bias concerns. We argue this "tabula rasa" data acquisition strategy is fundamentally inefficient. In this work, we propose Active Residual Learning, a new paradigm that leverages the observational model as a foundational prior. This approach shifts the experimental focus from learning target causal quantities from scratch to efficiently estimating the residuals required to correct observational bias. To operationalize this, we introduce the R-Design framework. Theoretically, we establish two key advantages: (1) a structural efficiency gap, proving that estimating smooth residual contrasts admits strictly faster convergence rates than reconstructing full outcomes; and (2) information efficiency, where we quantify the redundancy in standard parameter-based acquisition (e.g., BALD), demonstrating that such baselines waste budget on task-irrelevant nuisance uncertainty. We propose R-EPIG (Residual Expected Predictive Information Gain), a unified criterion that directly targets the causal estimand, minimizing residual uncertainty for estimation or clarifying decision boundaries for policy. Experiments on synthetic and semi-synthetic benchmarks demonstrate that R-Design significantly outperforms baselines, confirming that repairing a biased model is far more efficient than learning one from scratch.

