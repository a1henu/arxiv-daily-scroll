---
layout: default
title: Video Diffusion Models Excel at Tracking Similar-Looking Objects Without Supervision
---

# Video Diffusion Models Excel at Tracking Similar-Looking Objects Without Supervision
**arXiv**：[2512.02339v1](https://arxiv.org/abs/2512.02339) · [PDF](https://arxiv.org/pdf/2512.02339.pdf)  
**作者**：Chenshuang Zhang, Kang Zhang, Joon Son Chung, In So Kweon, Junmo Kim, Chengzhi Mao  

**一句话要点**：利用预训练视频扩散模型实现无监督跟踪视觉相似物体

**关键词**：视频扩散模型, 无监督跟踪, 视觉相似物体, 运动表示, 自监督学习

## 3 点简述
- 核心问题：视觉相似物体在运动区分上存在挑战，现有自监督跟踪器在视觉线索模糊时性能受限。
- 方法要点：发现视频扩散模型在去噪早期阶段自然学习到运动表示，无需任务特定训练即可用于跟踪。
- 实验或效果：在基准测试和新引入的视觉相似物体跟踪测试中，性能提升高达6点，可视化验证了鲁棒性。

## 摘要（原文）

> Distinguishing visually similar objects by their motion remains a critical challenge in computer vision. Although supervised trackers show promise, contemporary self-supervised trackers struggle when visual cues become ambiguous, limiting their scalability and generalization without extensive labeled data. We find that pre-trained video diffusion models inherently learn motion representations suitable for tracking without task-specific training. This ability arises because their denoising process isolates motion in early, high-noise stages, distinct from later appearance refinement. Capitalizing on this discovery, our self-supervised tracker significantly improves performance in distinguishing visually similar objects, an underexplored failure point for existing methods. Our method achieves up to a 6-point improvement over recent self-supervised approaches on established benchmarks and our newly introduced tests focused on tracking visually similar items. Visualizations confirm that these diffusion-derived motion representations enable robust tracking of even identical objects across challenging viewpoint changes and deformations.

