package set;

public class Set {

	private Object[] setElements;
	private int size;
	
	public int getSize() { return size;}
	
	public int getIndex(Object o) {
		for (int i=0; i<this.size; i++) {
			if (o == setElements[i]) {
				return i;
			}
		}
		return -1;
	}
	
	public boolean contains(Object o) {
			if (getIndex(o) != -1) {
				return true;
			}
		return false;
	}
	
	public void add(Object o) {
		if (contains(o)) {
			return;
		}
		setElements[size++] = o;
		size++;
	}
	
	public void remove(Object o) {
		if(contains(o)) {
			return;
		}
		
		Object temp = setElements[size]; 
		setElements[size] = setElements[getIndex(o)];
		setElements[getIndex(o)] = temp;
		
		Object[] newSet = new Object[size--];
		
		for (int i=0; i<size-1; i++) {
			newSet[i] = setElements[i];
		}
		
		setElements = newSet;
		size--;	
	}
			
	public Object[] intersection(Object[] otherSet) {
		int index = 0;
		Object[] interSets = new Object[size];
		for (int i=0; i<otherSet.length; i++) {
			if (contains(otherSet[i])) {
				interSets[index] = otherSet[i];
				index++;
			}
		}
		
		return interSets;
	}
}
