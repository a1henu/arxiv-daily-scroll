---
layout: default
title: Evaluating the Clinical Impact of Generative Inpainting on Bone Age Estimation
---

# Evaluating the Clinical Impact of Generative Inpainting on Bone Age Estimation
**arXiv**：[2511.23066v1](https://arxiv.org/abs/2511.23066) · [PDF](https://arxiv.org/pdf/2511.23066.pdf)  
**作者**：Felipe Akio Matsuoka, Eduardo Moreno J. M. Farina, Augusto Sarquis Serpa, Soraya Monteiro, Rodrigo Ragazzini, Nitamar Abdala, Marcelo Straus Takahashi, Felipe Campos Kitamura  

**一句话要点**：评估生成式修复对骨龄估计临床影响，发现性能显著下降

**关键词**：生成式修复, 骨龄估计, 医学图像分析, 临床AI验证, 深度学习集成

## 3 点简述
- 核心问题：生成式修复去除医学图像伪影是否影响AI临床性能，如骨龄和性别预测。
- 方法要点：使用RSNA骨龄数据集，生成600张修复图像，通过深度学习集成评估性能变化。
- 实验或效果：修复后骨龄MAE从6.26增至30.11个月，性别分类AUC从0.955降至0.704，显示结构改变。

## 摘要（原文）

> Generative foundation models can remove visual artifacts through realistic image inpainting, but their impact on medical AI performance remains uncertain. Pediatric hand radiographs often contain non-anatomical markers, and it is unclear whether inpainting these regions preserves features needed for bone age and gender prediction. To evaluate the clinical reliability of generative model-based inpainting for artifact removal, we used the RSNA Bone Age Challenge dataset, selecting 200 original radiographs and generating 600 inpainted versions with gpt-image-1 using natural language prompts to target non-anatomical artifacts. Downstream performance was assessed with deep learning ensembles for bone age estimation and gender classification, using mean absolute error (MAE) and area under the ROC curve (AUC) as metrics, and pixel intensity distributions to detect structural alterations. Inpainting markedly degraded model performance: bone age MAE increased from 6.26 to 30.11 months, and gender classification AUC decreased from 0.955 to 0.704. Inpainted images displayed pixel-intensity shifts and inconsistencies, indicating structural modifications not corrected by simple calibration. These findings show that, although visually realistic, foundation model-based inpainting can obscure subtle but clinically relevant features and introduce latent bias even when edits are confined to non-diagnostic regions, underscoring the need for rigorous, task-specific validation before integrating such generative tools into clinical AI workflows.

