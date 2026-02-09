---
layout: default
title: Same Answer, Different Representations: Hidden instability in VLMs
---

# Same Answer, Different Representations: Hidden instability in VLMs
**arXiv**：[2602.06652v1](https://arxiv.org/abs/2602.06652) · [PDF](https://arxiv.org/pdf/2602.06652.pdf)  
**作者**：Farooq Ahmad Wani, Alessandro Suglia, Rohit Saxena, Aryo Pradipta Gema, Wai-Chung Kwan, Fazl Barez, Maria Sofia Bucarelli, Fabrizio Silvestri, Pasquale Minervini  

**一句话要点**：提出表示感知与频率感知评估框架，揭示视觉语言模型内部表示不稳定性

**关键词**：视觉语言模型, 鲁棒性评估, 表示稳定性, 频谱分析, 多模态处理

## 3 点简述
- 核心问题：传统基于输出的鲁棒性评估假设稳定预测反映稳定多模态处理，但此假设不足。
- 方法要点：引入框架测量内部嵌入漂移、频谱敏感性和结构平滑性，结合标准标签指标。
- 实验或效果：在SEEDBench等数据集上发现三种失效模式，如表示漂移接近图像间变异性，且规模不提升鲁棒性。

## 摘要（原文）

> The robustness of Vision Language Models (VLMs) is commonly assessed through output-level invariance, implicitly assuming that stable predictions reflect stable multimodal processing. In this work, we argue that this assumption is insufficient. We introduce a representation-aware and frequency-aware evaluation framework that measures internal embedding drift, spectral sensitivity, and structural smoothness (spatial consistency of vision tokens), alongside standard label-based metrics. Applying this framework to modern VLMs across the SEEDBench, MMMU, and POPE datasets reveals three distinct failure modes. First, models frequently preserve predicted answers while undergoing substantial internal representation drift; for perturbations such as text overlays, this drift approaches the magnitude of inter-image variability, indicating that representations move to regions typically occupied by unrelated inputs despite unchanged outputs. Second, robustness does not improve with scale; larger models achieve higher accuracy but exhibit equal or greater sensitivity, consistent with sharper yet more fragile decision boundaries. Third, we find that perturbations affect tasks differently: they harm reasoning when they disrupt how models combine coarse and fine visual cues, but on the hallucination benchmarks, they can reduce false positives by making models generate more conservative answers.

