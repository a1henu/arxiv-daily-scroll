---
layout: default
title: Self-Paced and Self-Corrective Masked Prediction for Movie Trailer Generation
---

# Self-Paced and Self-Corrective Masked Prediction for Movie Trailer Generation
**arXiv**：[2512.04426v1](https://arxiv.org/abs/2512.04426) · [PDF](https://arxiv.org/pdf/2512.04426.pdf)  
**作者**：Sidan Zhu, Hongteng Xu, Dixin Luo  

**一句话要点**：提出自步自纠掩码预测方法SSMP，用于电影预告片生成，通过双向上下文建模和渐进自纠提升质量。

**关键词**：电影预告片生成, 自步学习, 掩码预测, Transformer编码器, 视频编辑

## 3 点简述
- 现有方法采用'选择-排序'范式，存在误差传播问题，限制预告片生成质量。
- SSMP基于Transformer编码器，通过自步掩码预测训练，实现双向上下文建模和渐进自纠机制。
- 定量结果和用户研究表明，SSMP在自动电影预告片生成中优于现有方法，达到先进水平。

## 摘要（原文）

> As a challenging video editing task, movie trailer generation involves selecting and reorganizing movie shots to create engaging trailers. Currently, most existing automatic trailer generation methods employ a "selection-then-ranking" paradigm (i.e., first selecting key shots and then ranking them), which suffers from inevitable error propagation and limits the quality of the generated trailers. Beyond this paradigm, we propose a new self-paced and self-corrective masked prediction method called SSMP, which achieves state-of-the-art results in automatic trailer generation via bi-directional contextual modeling and progressive self-correction. In particular, SSMP trains a Transformer encoder that takes the movie shot sequences as prompts and generates corresponding trailer shot sequences accordingly. The model is trained via masked prediction, reconstructing each trailer shot sequence from its randomly masked counterpart. The mask ratio is self-paced, allowing the task difficulty to adapt to the model and thereby improving model performance. When generating a movie trailer, the model fills the shot positions with high confidence at each step and re-masks the remaining positions for the next prediction, forming a progressive self-correction mechanism that is analogous to how human editors work. Both quantitative results and user studies demonstrate the superiority of SSMP in comparison to existing automatic movie trailer generation methods. Demo is available at: https://github.com/Dixin-Lab/SSMP.

