---
layout: default
title: Near-perfect photo-ID of the Hula painted frog with zero-shot deep local-feature matching
---

# Near-perfect photo-ID of the Hula painted frog with zero-shot deep local-feature matching
**arXiv**：[2601.08798v1](https://arxiv.org/abs/2601.08798) · [PDF](https://arxiv.org/pdf/2601.08798.pdf)  
**作者**：Maayan Yesharim, R. G. Bina Perl, Uri Roll, Sarig Gafny, Eli Geffen, Yoav Ram  

**一句话要点**：提出零样本深度局部特征匹配方法，实现胡拉彩蛙高精度非侵入式照片识别

**关键词**：零样本学习, 局部特征匹配, 照片识别, 两栖动物保护, 计算机视觉应用, 非侵入式监测

## 3 点简述
- 针对濒危两栖动物胡拉彩蛙，研究非侵入式个体照片识别以替代传统标记方法。
- 比较零样本深度局部特征匹配与全局特征嵌入模型，局部方法在闭集识别中达到98% top-1准确率。
- 开发两阶段工作流，结合全局特征检索与局部特征重排序，提升效率并保持高精度，部署为网页应用支持保护监测。

## 摘要（原文）

> Accurate individual identification is essential for monitoring rare amphibians, yet invasive marking is often unsuitable for critically endangered species. We evaluate state-of-the-art computer-vision methods for photographic re-identification of the Hula painted frog (Latonia nigriventer) using 1,233 ventral images from 191 individuals collected during 2013-2020 capture-recapture surveys. We compare deep local-feature matching in a zero-shot setting with deep global-feature embedding models. The local-feature pipeline achieves 98% top-1 closed-set identification accuracy, outperforming all global-feature models; fine-tuning improves the best global-feature model to 60% top-1 (91% top-10) but remains below local matching. To combine scalability with accuracy, we implement a two-stage workflow in which a fine-tuned global-feature model retrieves a short candidate list that is re-ranked by local-feature matching, reducing end-to-end runtime from 6.5-7.8 hours to ~38 minutes while maintaining ~96% top-1 closed-set accuracy on the labeled dataset. Separation of match scores between same- and different-individual pairs supports thresholding for open-set identification, enabling practical handling of novel individuals. We deploy this pipeline as a web application for routine field use, providing rapid, standardized, non-invasive identification to support conservation monitoring and capture-recapture analyses. Overall, in this species, zero-shot deep local-feature matching outperformed global-feature embedding and provides a strong default for photo-identification.

