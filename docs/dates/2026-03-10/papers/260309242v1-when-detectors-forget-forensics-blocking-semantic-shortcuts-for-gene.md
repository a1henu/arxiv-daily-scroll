---
layout: default
title: When Detectors Forget Forensics: Blocking Semantic Shortcuts for Generalizable AI-Generated Image Detection
---

# When Detectors Forget Forensics: Blocking Semantic Shortcuts for Generalizable AI-Generated Image Detection
**arXiv**：[2603.09242v1](https://arxiv.org/abs/2603.09242) · [PDF](https://arxiv.org/pdf/2603.09242.pdf)  
**作者**：Chao Shuai, Zhenguang Liu, Shaojing Fan, Bin Gong, Weichen Lian, Xiuli Bi, Zhongjie Ba, Kui Ren  

**一句话要点**：提出几何语义解耦模块以提升AI生成图像检测的泛化能力

**关键词**：AI生成图像检测, 语义解耦, 泛化能力, 视觉基础模型, 伪造痕迹检测

## 3 点简述
- 核心问题：基于视觉基础模型的检测器在分布偏移下依赖语义先验而非伪造痕迹，导致泛化失败
- 方法要点：利用冻结VFM作为语义引导，通过几何约束移除语义成分，强制检测器关注语义不变的伪造证据
- 实验或效果：在跨数据集评估中实现94.4%视频级AUC，对未见操作和通用场景检测均有提升

## 摘要（原文）

> AI-generated image detection has become increasingly important with the rapid advancement of generative AI. However, detectors built on Vision Foundation Models (VFMs, \emph{e.g.}, CLIP) often struggle to generalize to images created using unseen generation pipelines. We identify, for the first time, a key failure mechanism, termed \emph{semantic fallback}, where VFM-based detectors rely on dominant pre-trained semantic priors (such as identity) rather than forgery-specific traces under distribution shifts. To address this issue, we propose \textbf{Geometric Semantic Decoupling (GSD)}, a parameter-free module that explicitly removes semantic components from learned representations by leveraging a frozen VFM as a semantic guide with a trainable VFM as an artifact detector. GSD estimates semantic directions from batch-wise statistics and projects them out via a geometric constraint, forcing the artifact detector to rely on semantic-invariant forensic evidence. Extensive experiments demonstrate that our method consistently outperforms state-of-the-art approaches, achieving 94.4\% video-level AUC (+\textbf{1.2\%}) in cross-dataset evaluation, improving robustness to unseen manipulations (+\textbf{3.0\%} on DF40), and generalizing beyond faces to the detection of synthetic images of general scenes, including UniversalFakeDetect (+\textbf{0.9\%}) and GenImage (+\textbf{1.7\%}).

