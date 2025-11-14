---
layout: default
title: 3DFETUS: Standardizing Fetal Facial Planes in 3D Ultrasound
---

# 3DFETUS: Standardizing Fetal Facial Planes in 3D Ultrasound
**arXiv**：[2511.10412v1](https://arxiv.org/abs/2511.10412) · [PDF](https://arxiv.org/pdf/2511.10412.pdf)  
**作者**：Alomar Antonia, Rubio Ricardo, Albaiges Gerard, Salort-Benejam Laura, Caminal Julia, Prat Maria, Rueda Carolina, Cortes Berta, Piella Gemma, Sukno Federico  

**一句话要点**：提出GT++和3DFETUS以标准化胎儿3D超声面部平面定位

**关键词**：胎儿超声, 3D图像处理, 深度学习, 平面估计, 医学影像标准化

## 3 点简述
- 胎儿超声面部平面获取困难，因胎儿运动、方向变异和操作者依赖
- GT++基于解剖标志估计平面，3DFETUS用深度学习自动定位
- 实验显示平均平移误差4.13mm、旋转误差7.93度，临床评估有效

## 摘要（原文）

> Acquiring standard facial planes during routine fetal ultrasound (US) examinations is often challenging due to fetal movement, variability in orientation, and operator-dependent expertise. These factors contribute to inconsistencies, increased examination time, and potential diagnostic bias.
>   To address these challenges in the context of facial assessment, we present: 1) GT++, a robust algorithm that estimates standard facial planes from 3D US volumes using annotated anatomical landmarks; and 2) 3DFETUS, a deep learning model that automates and standardizes their localization in 3D fetal US volumes.
>   We evaluated our methods both qualitatively, through expert clinical review, and quantitatively. The proposed approach achieved a mean translation error of 4.13 mm and a mean rotation error of 7.93 degrees per plane, outperforming other state-of-the-art methods on 3D US volumes. Clinical assessments further confirmed the effectiveness of both GT++ and 3DFETUS, demonstrating statistically significant improvements in plane estimation accuracy.

