# Data-Mining-HW2
Code for 2025S-Data Mining Section 1 Group 7
> 本项目基于 [TSLib](https://github.com/thuml/Time-Series-Library) 中的 Autoformer, TimesNet 和 FEDformer 模型，实现了对时序数据的异常检测、评估与可视化。

---

## 🚀 Features

- 🔹 使用 **Autoformer** 模型进行滑动窗口级别的异常检测  
- 🔹 使用 **FEDformer** 模型进行频域增强的异常检测  
- 🔹 自动计算并输出 Precision、Recall、F1-score  
- 🔹 绘制并保存异常点可视化图表  
- 🔹 一键式运行脚本，快速复现实验流程  

---

## 🛠 Tech Stack

- **语言**：Python 3.8+  
- **深度学习框架**：PyTorch  
- **时序分析库**：TSLib  
- **数据处理**：NumPy、Pandas  
- **可视化**：Matplotlib  
- **配置管理**：YAML  

---

## 📦 Installation

```bash
# 1. 克隆仓库
gh repo clone htupeilrahc/Data-Mining-HW2

# 2. 安装依赖
pip install -r requirements.txt

# 3.运行脚本
bash ./scripts/anomaly_detection/Tube/Autoformer_Tube.sh
