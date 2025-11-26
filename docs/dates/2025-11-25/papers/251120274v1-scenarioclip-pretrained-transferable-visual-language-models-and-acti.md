---
layout: default
title: ScenarioCLIP: Pretrained Transferable Visual Language Models and Action-Genome Dataset for Natural Scene Analysis
---

# ScenarioCLIP: Pretrained Transferable Visual Language Models and Action-Genome Dataset for Natural Scene Analysis
**arXiv**：[2511.20274v1](https://arxiv.org/abs/2511.20274) · [PDF](https://arxiv.org/pdf/2511.20274.pdf)  
**作者**：Advik Sinha, Saurabh Atreya, Aashutosh A, Sk Aziz Ali, Abhijit Das  

**一句话要点**：提出ScenarioCLIP模型和Action-Genome数据集，用于自然场景的多对象关系分析

**关键词**：视觉语言模型, 场景分析, 跨模态检索, 关系建模, 数据集构建, 零样本学习

## 3 点简述
- 核心问题：现有CLIP模型缺乏对场景中多对象和动作关系的显式建模
- 方法要点：结合文本、接地关系和图像输入，预训练并微调以提升跨模态检索能力
- 实验或效果：在多种场景任务中展示零样本和微调性能，优于基线方法

## 摘要（原文）

> Until recently, the general corpus of CLIP-type fundamental models has widely explored either the retrieval of short descriptions or the classification of objects in the scene as SINGLE-object image classification task. The same holds for retrieving the image embedding (image retrieval task) given a text prompt. However, real-world scene images exhibit rich compositional structure involving multiple objects and actions. The latest methods in the CLIP-based literature improve class-level discrimination by mining harder negative image-text pairs and by refining permanent text prompts, often using LLMs. However, these improvements remain confined to predefined class lists and do not explicitly model relational or compositional structure. PyramidCLIP partially addresses this gap by aligning global and local visual features, yet it still lacks explicit modeling of inter-object relations. Hence, to further leverage this aspect for scene analysis, the proposed ScenarioCLIP model accepts input texts, grounded relations, and input images, along with focused regions highlighting relations. The proposed model is pretrained on curated scenario data, and finetuned for specialized downstream tasks, such as cross-modal retrieval and fine-grained visual understanding tasks. To address the lack of domain-specific datasets, we generate a novel dataset by extending image-text pairs from existing diverse indoor and outdoor scenario datasets that are publicly available. We used a pipeline of existing language models to ground action, object, and relations, filled by manual and automatic curation. We established a comprehensive benchmark for several scenario-based tasks and compared it with many baseline methods. ScenarioCLIP demonstrates robust zero-shot and finetune performance on various domain-specific tasks. Our code and dataset are available at https://github.com/scenario-clip/ScenarioCLIP

