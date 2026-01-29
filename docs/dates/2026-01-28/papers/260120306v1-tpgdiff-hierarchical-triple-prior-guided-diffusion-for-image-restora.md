---
layout: default
title: TPGDiff: Hierarchical Triple-Prior Guided Diffusion for Image Restoration
---

# TPGDiff: Hierarchical Triple-Prior Guided Diffusion for Image Restoration
**arXiv**：[2601.20306v1](https://arxiv.org/abs/2601.20306) · [PDF](https://arxiv.org/pdf/2601.20306.pdf)  
**作者**：Yanjie Tu, Qingsen Yan, Axi Niu, Jiacong Tang  

**一句话要点**：提出TPGDiff，通过分层三重先验引导扩散模型解决统一图像修复中严重退化区域内容重建问题。

**关键词**：图像修复, 扩散模型, 先验引导, 分层结构, 语义提取, 退化提取

## 3 点简述
- 核心问题：现有方法依赖退化先验，但在严重退化区域内容重建困难，且浅层引入语义信息易破坏空间结构。
- 方法要点：结合退化、结构和语义三重先验，分层引导扩散过程，结构先验用于浅层细节捕获，语义先验用于深层高级指导。
- 实验或效果：在单/多退化基准测试中表现优异，实现跨场景的优越性能和泛化能力。

## 摘要（原文）

> All-in-one image restoration aims to address diverse degradation types using a single unified model. Existing methods typically rely on degradation priors to guide restoration, yet often struggle to reconstruct content in severely degraded regions. Although recent works leverage semantic information to facilitate content generation, integrating it into the shallow layers of diffusion models often disrupts spatial structures (\emph{e.g.}, blurring artifacts). To address this issue, we propose a Triple-Prior Guided Diffusion (TPGDiff) network for unified image restoration. TPGDiff incorporates degradation priors throughout the diffusion trajectory, while introducing structural priors into shallow layers and semantic priors into deep layers, enabling hierarchical and complementary prior guidance for image reconstruction. Specifically, we leverage multi-source structural cues as structural priors to capture fine-grained details and guide shallow layers representations. To complement this design, we further develop a distillation-driven semantic extractor that yields robust semantic priors, ensuring reliable high-level guidance at deep layers even under severe degradations. Furthermore, a degradation extractor is employed to learn degradation-aware priors, enabling stage-adaptive control of the diffusion process across all timesteps. Extensive experiments on both single- and multi-degradation benchmarks demonstrate that TPGDiff achieves superior performance and generalization across diverse restoration scenarios. Our project page is: https://leoyjtu.github.io/tpgdiff-project.

