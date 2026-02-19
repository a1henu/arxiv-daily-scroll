---
layout: default
title: Evaluating Demographic Misrepresentation in Image-to-Image Portrait Editing
---

# Evaluating Demographic Misrepresentation in Image-to-Image Portrait Editing
**arXiv**：[2602.16149v1](https://arxiv.org/abs/2602.16149) · [PDF](https://arxiv.org/pdf/2602.16149.pdf)  
**作者**：Huichan Seo, Minki Hong, Sieun Choi, Jihie Kim, Jean Oh  

**一句话要点**：提出评估图像到图像肖像编辑中人口统计误表示的方法，揭示身份保留失败的不均衡性。

**关键词**：图像到图像编辑, 人口统计偏差, 身份保留, 视觉语言模型, 刻板印象替换, 软擦除

## 3 点简述
- 核心问题：探索指令引导图像编辑中人口统计条件失败，如软擦除和刻板印象替换。
- 方法要点：构建控制基准，使用诊断提示集生成和编辑肖像，结合VLM评分和人工评估。
- 实验或效果：发现身份保留失败普遍且不均衡，提示级约束可减少少数群体人口统计变化。

## 摘要（原文）

> Demographic bias in text-to-image (T2I) generation is well studied, yet demographic-conditioned failures in instruction-guided image-to-image (I2I) editing remain underexplored. We examine whether identical edit instructions yield systematically different outcomes across subject demographics in open-weight I2I editors. We formalize two failure modes: Soft Erasure, where edits are silently weakened or ignored in the output image, and Stereotype Replacement, where edits introduce unrequested, stereotype-consistent attributes. We introduce a controlled benchmark that probes demographic-conditioned behavior by generating and editing portraits conditioned on race, gender, and age using a diagnostic prompt set, and evaluate multiple editors with vision-language model (VLM) scoring and human evaluation. Our analysis shows that identity preservation failures are pervasive, demographically uneven, and shaped by implicit social priors, including occupation-driven gender inference. Finally, we demonstrate that a prompt-level identity constraint, without model updates, can substantially reduce demographic change for minority groups while leaving majority-group portraits largely unchanged, revealing asymmetric identity priors in current editors. Together, our findings establish identity preservation as a central and demographically uneven failure mode in I2I editing and motivate demographic-robust editing systems. Project page: https://seochan99.github.io/i2i-demographic-bias

