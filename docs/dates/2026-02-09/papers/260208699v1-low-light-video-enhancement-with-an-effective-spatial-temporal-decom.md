---
layout: default
title: Low-Light Video Enhancement with An Effective Spatial-Temporal Decomposition Paradigm
---

# Low-Light Video Enhancement with An Effective Spatial-Temporal Decomposition Paradigm
**arXiv**：[2602.08699v1](https://arxiv.org/abs/2602.08699) · [PDF](https://arxiv.org/pdf/2602.08699.pdf)  
**作者**：Xiaogang Xu, Kun Zhou, Tao Hu, Jiafei Wu, Ruixing Wang, Hao Peng, Bei Yu  

**一句话要点**：提出基于视点感知分解的VLLVE++框架，以增强低光视频的可见性与一致性。

**关键词**：低光视频增强, 时空分解, 视点感知, 残差学习, 双向学习, 视频基准测试

## 3 点简述
- 核心问题：低光视频存在严重不可见性和噪声，需恢复动态或静态场景。
- 方法要点：引入视点无关与视点相关分解，结合残差项和双向学习提升内容捕获能力。
- 实验或效果：在广泛基准测试中验证，能有效处理真实场景和高动态视频。

## 摘要（原文）

> Low-Light Video Enhancement (LLVE) seeks to restore dynamic or static scenes plagued by severe invisibility and noise. In this paper, we present an innovative video decomposition strategy that incorporates view-independent and view-dependent components to enhance the performance of LLVE. The framework is called View-aware Low-light Video Enhancement (VLLVE). We leverage dynamic cross-frame correspondences for the view-independent term (which primarily captures intrinsic appearance) and impose a scene-level continuity constraint on the view-dependent term (which mainly describes the shading condition) to achieve consistent and satisfactory decomposition results. To further ensure consistent decomposition, we introduce a dual-structure enhancement network featuring a cross-frame interaction mechanism. By supervising different frames simultaneously, this network encourages them to exhibit matching decomposition features. This mechanism can seamlessly integrate with encoder-decoder single-frame networks, incurring minimal additional parameter costs. Building upon VLLVE, we propose a more comprehensive decomposition strategy by introducing an additive residual term, resulting in VLLVE++. This residual term can simulate scene-adaptive degradations, which are difficult to model using a decomposition formulation for common scenes, thereby further enhancing the ability to capture the overall content of videos. In addition, VLLVE++ enables bidirectional learning for both enhancement and degradation-aware correspondence refinement (end-to-end manner), effectively increasing reliable correspondences while filtering out incorrect ones. Notably, VLLVE++ demonstrates strong capability in handling challenging cases, such as real-world scenes and videos with high dynamics. Extensive experiments are conducted on widely recognized LLVE benchmarks.

