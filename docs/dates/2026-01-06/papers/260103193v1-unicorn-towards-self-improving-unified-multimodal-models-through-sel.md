---
layout: default
title: UniCorn: Towards Self-Improving Unified Multimodal Models through Self-Generated Supervision
---

# UniCorn: Towards Self-Improving Unified Multimodal Models through Self-Generated Supervision
**arXiv**：[2601.03193v1](https://arxiv.org/abs/2601.03193) · [PDF](https://arxiv.org/pdf/2601.03193.pdf)  
**作者**：Ruiyan Han, Zhen Fang, XinYu Sun, Yuchen Ma, Ziheng Wang, Yu Zeng, Zehui Chen, Lin Chen, Wenxuan Huang, Wei-Jie Xu, Yi Cao, Feng Zhao  

**一句话要点**：提出UniCorn框架，通过自生成监督解决统一多模态模型在生成任务中的传导性失语问题。

**关键词**：统一多模态模型, 自生成监督, 传导性失语, 自改进框架, 图像生成, 认知模式重构

## 3 点简述
- 核心问题：统一多模态模型存在传导性失语，即理解多模态输入但生成质量不足。
- 方法要点：将模型分为提议者、求解者和评判者角色，通过自博弈和认知模式重构实现自改进。
- 实验或效果：在六个图像生成基准上显著提升性能，包括TIIF、DPG、CompBench和UniCycle等。

## 摘要（原文）

> While Unified Multimodal Models (UMMs) have achieved remarkable success in cross-modal comprehension, a significant gap persists in their ability to leverage such internal knowledge for high-quality generation. We formalize this discrepancy as Conduction Aphasia, a phenomenon where models accurately interpret multimodal inputs but struggle to translate that understanding into faithful and controllable synthesis. To address this, we propose UniCorn, a simple yet elegant self-improvement framework that eliminates the need for external data or teacher supervision. By partitioning a single UMM into three collaborative roles: Proposer, Solver, and Judge, UniCorn generates high-quality interactions via self-play and employs cognitive pattern reconstruction to distill latent understanding into explicit generative signals. To validate the restoration of multimodal coherence, we introduce UniCycle, a cycle-consistency benchmark based on a Text to Image to Text reconstruction loop. Extensive experiments demonstrate that UniCorn achieves comprehensive and substantial improvements over the base model across six general image generation benchmarks. Notably, it achieves SOTA performance on TIIF(73.8), DPG(86.8), CompBench(88.5), and UniCycle while further delivering substantial gains of +5.0 on WISE and +6.5 on OneIG. These results highlight that our method significantly enhances T2I generation while maintaining robust comprehension, demonstrating the scalability of fully self-supervised refinement for unified multimodal intelligence.

