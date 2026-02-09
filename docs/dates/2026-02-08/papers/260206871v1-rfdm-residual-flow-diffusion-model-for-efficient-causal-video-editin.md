---
layout: default
title: RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing
---

# RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing
**arXiv**：[2602.06871v1](https://arxiv.org/abs/2602.06871) · [PDF](https://arxiv.org/pdf/2602.06871.pdf)  
**作者**：Mohammadreza Salehi, Mehdi Noroozi, Luca Morreale, Ruchika Chavhan, Malcolm Chadwick, Alberto Gil Ramos, Abhinav Mehrotra  

**一句话要点**：提出残差流扩散模型以实现高效因果视频编辑，支持变长视频的自然语言控制编辑。

**关键词**：视频编辑, 扩散模型, 因果建模, 残差学习, 变长视频处理, 自然语言控制

## 3 点简述
- 核心问题：现有视频编辑方法通常需要固定长度输入且计算量大，而自回归视频生成在编辑中应用不足。
- 方法要点：基于2D图像扩散模型，通过条件化前一帧预测实现视频编辑，并引入残差流扩散以聚焦帧间变化。
- 实验或效果：在风格迁移和对象移除任务上超越基于图像的方法，与3D视频模型竞争，计算效率高且独立于视频长度。

## 摘要（原文）

> Instructional video editing applies edits to an input video using only text prompts, enabling intuitive natural-language control. Despite rapid progress, most methods still require fixed-length inputs and substantial compute. Meanwhile, autoregressive video generation enables efficient variable-length synthesis, yet remains under-explored for video editing. We introduce a causal, efficient video editing model that edits variable-length videos frame by frame. For efficiency, we start from a 2D image-to-image (I2I) diffusion model and adapt it to video-to-video (V2V) editing by conditioning the edit at time step t on the model's prediction at t-1. To leverage videos' temporal redundancy, we propose a new I2I diffusion forward process formulation that encourages the model to predict the residual between the target output and the previous prediction. We call this Residual Flow Diffusion Model (RFDM), which focuses the denoising process on changes between consecutive frames. Moreover, we propose a new benchmark that better ranks state-of-the-art methods for editing tasks. Trained on paired video data for global/local style transfer and object removal, RFDM surpasses I2I-based methods and competes with fully spatiotemporal (3D) V2V models, while matching the compute of image models and scaling independently of input video length. More content can be found in: https://smsd75.github.io/RFDM_page/

