---
layout: default
title: DisMo: Disentangled Motion Representations for Open-World Motion Transfer
---

# DisMo: Disentangled Motion Representations for Open-World Motion Transfer
**arXiv**：[2511.23428v1](https://arxiv.org/abs/2511.23428) · [PDF](https://arxiv.org/pdf/2511.23428.pdf)  
**作者**：Thomas Ressler-Antal, Frank Fundel, Malek Ben Alaya, Stefan Andreas Baumann, Felix Krause, Ming Gui, Björn Ommer  

**一句话要点**：提出DisMo以学习解耦的运动表示，实现开放世界运动迁移

**关键词**：运动表示学习, 开放世界运动迁移, 视频生成, 解耦表示, 零样本分类

## 3 点简述
- 现有文本/图像到视频模型缺乏显式运动表示，限制内容创作应用
- 通过图像空间重建目标从原始视频学习通用运动表示，独立于外观和姿态
- 在运动迁移任务中表现优异，并在零样本动作分类上超越V-JEPA等模型

## 摘要（原文）

> Recent advances in text-to-video (T2V) and image-to-video (I2V) models, have enabled the creation of visually compelling and dynamic videos from simple textual descriptions or initial frames. However, these models often fail to provide an explicit representation of motion separate from content, limiting their applicability for content creators. To address this gap, we propose DisMo, a novel paradigm for learning abstract motion representations directly from raw video data via an image-space reconstruction objective. Our representation is generic and independent of static information such as appearance, object identity, or pose. This enables open-world motion transfer, allowing motion to be transferred across semantically unrelated entities without requiring object correspondences, even between vastly different categories. Unlike prior methods, which trade off motion fidelity and prompt adherence, are overfitting to source structure or drifting from the described action, our approach disentangles motion semantics from appearance, enabling accurate transfer and faithful conditioning. Furthermore, our motion representation can be combined with any existing video generator via lightweight adapters, allowing us to effortlessly benefit from future advancements in video models. We demonstrate the effectiveness of our method through a diverse set of motion transfer tasks. Finally, we show that the learned representations are well-suited for downstream motion understanding tasks, consistently outperforming state-of-the-art video representation models such as V-JEPA in zero-shot action classification on benchmarks including Something-Something v2 and Jester. Project page: https://compvis.github.io/DisMo

