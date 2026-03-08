---
layout: default
title: Digital Twin Driven Textile Classification and Foreign Object Recognition in Automated Sorting Systems
---

# Digital Twin Driven Textile Classification and Foreign Object Recognition in Automated Sorting Systems
**arXiv**：[2603.05230v1](https://arxiv.org/abs/2603.05230) · [PDF](https://arxiv.org/pdf/2603.05230.pdf)  
**作者**：Serkan Ergun, Tobias Mitterer, Hubert Zangl  

**一句话要点**：提出数字孪生驱动的机器人分拣系统，结合视觉语言模型和感知技术，实现现实工业场景中的纺织品分类与异物识别。

**关键词**：数字孪生, 机器人分拣, 视觉语言模型, 纺织品分类, 异物检测, 多模态感知

## 3 点简述
- 核心问题：可持续纺织品回收需自动化处理变形衣物和杂乱环境中的异物检测。
- 方法要点：集成抓取预测、多模态感知和语义推理，利用数字孪生和MoveIt进行碰撞感知路径规划。
- 实验或效果：在223个场景数据集上评估9个VLM，Qwen模型家族最高准确率达87.9%，Gemma3在边缘部署中提供速度与精度平衡。

## 摘要（原文）

> The increasing demand for sustainable textile recycling requires robust automation solutions capable of handling deformable garments and detecting foreign objects in cluttered environments. This work presents a digital twin driven robotic sorting system that integrates grasp prediction, multi modal perception, and semantic reasoning for real world textile classification. A dual arm robotic cell equipped with RGBD sensing, capacitive tactile feedback, and collision-aware motion planning autonomously separates garments from an unsorted basket, transfers them to an inspection zone, and classifies them using state of the art Visual Language Models (VLMs). We benchmark nine VLM s from five model families on a dataset of 223 inspection scenarios comprising shirts, socks, trousers, underwear, foreign objects (including garments outside of the aforementioned classes), and empty scenes. The evaluation assesses per class accuracy, hallucination behavior, and computational performance under practical hardware constraints. Results show that the Qwen model family achieves the highest overall accuracy (up to 87.9 %), with strong foreign object detection performance, while lighter models such as Gemma3 offer competitive speed accuracy trade offs for edge deployment. A digital twin combined with MoveIt enables collision aware path planning and integrates segmented 3D point clouds of inspected garments into the virtual environment for improved manipulation reliability. The presented system demonstrates the feasibility of combining semantic VLM reasoning with conventional grasp detection and digital twin technology for scalable, autonomous textile sorting in realistic industrial settings.

