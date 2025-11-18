---
layout: default
title: Descriptor: Distance-Annotated Traffic Perception Question Answering (DTPQA)
---

# Descriptor: Distance-Annotated Traffic Perception Question Answering (DTPQA)
**arXiv**：[2511.13397v1](https://arxiv.org/abs/2511.13397) · [PDF](https://arxiv.org/pdf/2511.13397.pdf)  
**作者**：Nikos Theodoridis, Tim Brophy, Reenu Mohandas, Ganesh Sistu, Fiachra Collins, Anthony Scanlan, Ciaran Eising  

**一句话要点**：提出距离标注交通感知问答基准DTPQA，用于评估视觉语言模型在自动驾驶场景中的感知能力。

**关键词**：视觉语言模型, 交通场景感知, 距离标注基准, 自动驾驶评估, 视觉问答

## 3 点简述
- 核心问题：自动驾驶中视觉语言模型需具备鲁棒感知能力，尤其在复杂交通场景和远距离对象识别。
- 方法要点：构建合成和真实世界基准，包含图像、问题、答案和对象距离标注，以隔离感知评估。
- 实验或效果：提供数据集和Python脚本，支持分析模型性能随对象距离增加而下降的情况。

## 摘要（原文）

> The remarkable progress of Vision-Language Models (VLMs) on a variety of tasks has raised interest in their application to automated driving. However, for these models to be trusted in such a safety-critical domain, they must first possess robust perception capabilities, i.e., they must be capable of understanding a traffic scene, which can often be highly complex, with many things happening simultaneously. Moreover, since critical objects and agents in traffic scenes are often at long distances, we require systems with not only strong perception capabilities at close distances (up to 20 meters), but also at long (30+ meters) range. Therefore, it is important to evaluate the perception capabilities of these models in isolation from other skills like reasoning or advanced world knowledge. Distance-Annotated Traffic Perception Question Answering (DTPQA) is a Visual Question Answering (VQA) benchmark designed specifically for this purpose: it can be used to evaluate the perception systems of VLMs in traffic scenarios using trivial yet crucial questions relevant to driving decisions. It consists of two parts: a synthetic benchmark (DTP-Synthetic) created using a simulator, and a real-world benchmark (DTP-Real) built on top of existing images of real traffic scenes. Additionally, DTPQA includes distance annotations, i.e., how far the object in question is from the camera. More specifically, each DTPQA sample consists of (at least): (a) an image, (b) a question, (c) the ground truth answer, and (d) the distance of the object in question, enabling analysis of how VLM performance degrades with increasing object distance. In this article, we provide the dataset itself along with the Python scripts used to create it, which can be used to generate additional data of the same kind.

