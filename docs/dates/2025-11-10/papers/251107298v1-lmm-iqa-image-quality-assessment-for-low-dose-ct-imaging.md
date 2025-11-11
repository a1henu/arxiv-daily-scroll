---
layout: default
title: LMM-IQA: Image Quality Assessment for Low-Dose CT Imaging
---

# LMM-IQA: Image Quality Assessment for Low-Dose CT Imaging
**arXiv**：[2511.07298v1](https://arxiv.org/abs/2511.07298) · [PDF](https://arxiv.org/pdf/2511.07298.pdf)  
**作者**：Kagan Celik, Mehmet Ozan Unal, Metin Ertas, Isa Yildirim  

**一句话要点**：提出基于LLM的低剂量CT图像质量评估系统，生成分数与文本描述以提升临床工作流。

**关键词**：低剂量CT, 图像质量评估, LLM应用, 噪声分析, 临床工作流, 可解释AI

## 3 点简述
- 低剂量CT降低辐射但引入噪声、模糊和对比度损失，影响诊断质量。
- 系统使用LLM生成数值分数和退化文本描述，并探索零样本、元数据集成和错误反馈等推理策略。
- 评估结果与人类判断高度相关，提供可解释输出，代码已开源。

## 摘要（原文）

> Low-dose computed tomography (CT) represents a significant improvement in
> patient safety through lower radiation doses, but increased noise, blur, and
> contrast loss can diminish diagnostic quality. Therefore, consistency and
> robustness in image quality assessment become essential for clinical
> applications. In this study, we propose an LLM-based quality assessment system
> that generates both numerical scores and textual descriptions of degradations
> such as noise, blur, and contrast loss. Furthermore, various inference
> strategies - from the zero-shot approach to metadata integration and error
> feedback - are systematically examined, demonstrating the progressive
> contribution of each method to overall performance. The resultant assessments
> yield not only highly correlated scores but also interpretable output, thereby
> adding value to clinical workflows. The source codes of our study are available
> at https://github.com/itu-biai/lmms_ldct_iqa.

