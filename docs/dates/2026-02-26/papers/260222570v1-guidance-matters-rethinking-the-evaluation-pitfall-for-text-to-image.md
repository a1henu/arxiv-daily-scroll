---
layout: default
title: Guidance Matters: Rethinking the Evaluation Pitfall for Text-to-Image Generation
---

# Guidance Matters: Rethinking the Evaluation Pitfall for Text-to-Image Generation
**arXiv**：[2602.22570v1](https://arxiv.org/abs/2602.22570) · [PDF](https://arxiv.org/pdf/2602.22570.pdf)  
**作者**：Dian Xie, Shitong Shao, Lichen Bai, Zikai Zhou, Bojun Cheng, Shuo Yang, Jun Wu, Zeke Xie  

**一句话要点**：揭示扩散引导评估陷阱并提出公平评估框架，以重新审视文本到图像生成方法

**关键词**：扩散模型, 文本到图像生成, 评估陷阱, 引导尺度, 公平比较, 人类偏好

## 3 点简述
- 发现常见人类偏好模型对高引导尺度有强偏见，导致评估失真
- 提出引导感知评估框架，通过尺度校准实现公平比较
- 实验显示仅增加CFG尺度可与多数方法竞争，但所有方法在公平评估下表现下降

## 摘要（原文）

> Classifier-free guidance (CFG) has helped diffusion models achieve great conditional generation in various fields. Recently, more diffusion guidance methods have emerged with improved generation quality and human preference. However, can these emerging diffusion guidance methods really achieve solid and significant improvements? In this paper, we rethink recent progress on diffusion guidance. Our work mainly consists of four contributions. First, we reveal a critical evaluation pitfall that common human preference models exhibit a strong bias towards large guidance scales. Simply increasing the CFG scale can easily improve quantitative evaluation scores due to strong semantic alignment, even if image quality is severely damaged (e.g., oversaturation and artifacts). Second, we introduce a novel guidance-aware evaluation (GA-Eval) framework that employs effective guidance scale calibration to enable fair comparison between current guidance methods and CFG by identifying the effects orthogonal and parallel to CFG effects. Third, motivated by the evaluation pitfall, we design Transcendent Diffusion Guidance (TDG) method that can significantly improve human preference scores in the conventional evaluation framework but actually does not work in practice. Fourth, in extensive experiments, we empirically evaluate recent eight diffusion guidance methods within the conventional evaluation framework and the proposed GA-Eval framework. Notably, simply increasing the CFG scales can compete with most studied diffusion guidance methods, while all methods suffer severely from winning rate degradation over standard CFG. Our work would strongly motivate the community to rethink the evaluation paradigm and future directions of this field.

