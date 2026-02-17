---
layout: default
title: Error Patterns in Historical OCR: A Comparative Analysis of TrOCR and a Vision-Language Model
---

# Error Patterns in Historical OCR: A Comparative Analysis of TrOCR and a Vision-Language Model
**arXiv**：[2602.14524v1](https://arxiv.org/abs/2602.14524) · [PDF](https://arxiv.org/pdf/2602.14524.pdf)  
**作者**：Ari Vesalainen, Eetu Mäkelä, Laura Ruotsalainen, Mikko Tolonen  

**一句话要点**：比较TrOCR与Qwen在历史OCR中的错误模式，揭示架构偏差对学术风险的影响

**关键词**：历史OCR, 错误分析, 视觉语言模型, TrOCR, Qwen, 架构偏差

## 3 点简述
- 核心问题：历史印刷文本OCR因质量退化、古字形和非标准化拼写而具挑战性，聚合准确率指标不足以评估学术可靠性
- 方法要点：使用长度加权准确率指标和假设驱动错误分析，比较专用OCR模型TrOCR与通用视觉语言模型Qwen
- 实验或效果：Qwen准确率更高但可能静默正则化历史形式，TrOCR保真度更一致但易传播错误，架构偏差系统影响错误结构

## 摘要（原文）

> Optical Character Recognition (OCR) of eighteenth-century printed texts remains challenging due to degraded print quality, archaic glyphs, and non-standardized orthography. Although transformer-based OCR systems and Vision-Language Models (VLMs) achieve strong aggregate accuracy, metrics such as Character Error Rate (CER) and Word Error Rate (WER) provide limited insight into their reliability for scholarly use. We compare a dedicated OCR transformer (TrOCR) and a general-purpose Vision-Language Model (Qwen) on line-level historical English texts using length-weighted accuracy metrics and hypothesis driven error analysis.
>   While Qwen achieves lower CER/WER and greater robustness to degraded input, it exhibits selective linguistic regularization and orthographic normalization that may silently alter historically meaningful forms. TrOCR preserves orthographic fidelity more consistently but is more prone to cascading error propagation. Our findings show that architectural inductive biases shape OCR error structure in systematic ways. Models with similar aggregate accuracy can differ substantially in error locality, detectability, and downstream scholarly risk, underscoring the need for architecture-aware evaluation in historical digitization workflows.

