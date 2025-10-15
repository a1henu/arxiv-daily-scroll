---
layout: default
title: DIANet: A Phase-Aware Dual-Stream Network for Micro-Expression Recognition via Dynamic Images
---

# DIANet: A Phase-Aware Dual-Stream Network for Micro-Expression Recognition via Dynamic Images
**arXiv**：[2510.12219v1](https://arxiv.org/abs/2510.12219) · [PDF](https://arxiv.org/pdf/2510.12219.pdf)  
**作者**：Vu Tram Anh Khuong, Luu Tu Nguyen, Thi Bich Phuong Man, Thanh Ha Le, Thi Duyen Ngo  

**一句话要点**：提出DIANet双流网络，通过相位感知动态图像解决微表情识别中忽略不同时间相位的问题。

**关键词**：微表情识别, 动态图像, 双流网络, 相位感知, 交叉注意力, 时间建模

## 3 点简述
- 核心问题：微表情识别因表情短暂、数据稀缺及传统方法忽略不同时间相位特征而困难。
- 方法要点：使用双流网络分别处理起始到顶点和顶点到结束相位，并采用交叉注意力融合模块。
- 实验或效果：在多个基准数据集上优于单相位方法，验证了建模时间相位的重要性。

## 摘要（原文）

> Micro-expressions are brief, involuntary facial movements that typically last
> less than half a second and often reveal genuine emotions. Accurately
> recognizing these subtle expressions is critical for applications in
> psychology, security, and behavioral analysis. However, micro-expression
> recognition (MER) remains a challenging task due to the subtle and transient
> nature of facial cues and the limited availability of annotated data. While
> dynamic image (DI) representations have been introduced to summarize temporal
> motion into a single frame, conventional DI-based methods often overlook the
> distinct characteristics of different temporal phases within a
> micro-expression. To address this issue, this paper proposes a novel
> dual-stream framework, DIANet, which leverages phase-aware dynamic images - one
> encoding the onset-to-apex phase and the other capturing the apex-to-offset
> phase. Each stream is processed by a dedicated convolutional neural network,
> and a cross-attention fusion module is employed to adaptively integrate
> features from both streams based on their contextual relevance. Extensive
> experiments conducted on three benchmark MER datasets (CASME-II, SAMM, and
> MMEW) demonstrate that the proposed method consistently outperforms
> conventional single-phase DI-based approaches. The results highlight the
> importance of modeling temporal phase information explicitly and suggest a
> promising direction for advancing MER.

