---
layout: default
title: LocateAnything3D: Vision-Language 3D Detection with Chain-of-Sight
---

# LocateAnything3D: Vision-Language 3D Detection with Chain-of-Sight
**arXiv**：[2511.20648v1](https://arxiv.org/abs/2511.20648) · [PDF](https://arxiv.org/pdf/2511.20648.pdf)  
**作者**：Yunze Man, Shihao Wang, Guowen Zhang, Johan Bjorck, Zhiqi Li, Liang-Yan Gui, Jim Fan, Jan Kautz, Yu-Xiong Wang, Zhiding Yu  

**一句话要点**：提出LocateAnything3D方法，通过链式视觉推理实现开放词汇3D检测

**关键词**：3D检测, 视觉语言模型, 链式视觉推理, 开放词汇检测, 零样本泛化, 边界框预测

## 3 点简述
- 核心问题：现有视觉语言模型缺乏多对象3D检测能力，难以在3D空间中定位物体
- 方法要点：采用链式视觉序列，先预测2D检测，再按从近到远顺序预测3D边界框
- 实验或效果：在Omni3D基准上达到49.89 AP_3D，零样本泛化能力强

## 摘要（原文）

> To act in the world, a model must name what it sees and know where it is in 3D. Today's vision-language models (VLMs) excel at open-ended 2D description and grounding, yet multi-object 3D detection remains largely missing from the VLM toolbox. We present LocateAnything3D, a VLM-native recipe that casts 3D detection as a next-token prediction problem. The key is a short, explicit Chain-of-Sight (CoS) sequence that mirrors how human reason from images: find an object in 2D, then infer its distance, size, and pose. The decoder first emits 2D detections as a visual chain-of-thought, then predicts 3D boxes under an easy-to-hard curriculum: across objects, a near-to-far order reduces early ambiguity and matches ego-centric utility; within each object, a center-from-camera, dimensions, and rotation factorization ranks information by stability and learnability. This VLM-native interface preserves open-vocabulary and visual-prompting capability without specialized heads. On the challenging Omni3D benchmark, our model achieves state-of-the-art results, with 49.89 AP_3D, surpassing the previous best by +15.51 absolute improvement even when the baseline is given ground-truth 2D boxes. It also generalizes zero-shot to held-out categories with strong robustness. By turning 3D detection into a disciplined next-token problem, LocateAnything3D offers a practical foundation for models to perceive in 3D.

